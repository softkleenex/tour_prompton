# 🔌 29. 기상청 생활기상지수 조회 서비스_GW (Living Weather API Spec)

> **본 문서는 AI 에이전트 '크리넥스(Kleenex)'의 두 번째 심장인 [생활 기상 안전 에이전트]가 실시간으로 호출할 기상청 생활기상지수 조회 OpenAPI 규격서입니다. 엔노이아(ennoia) API 커넥터에 그대로 복사-붙여넣기하여 바인딩할 수 있도록 JSON 및 파라미터 매핑 가이드를 제공합니다.**

---

## 🌐 1. API 기본 정보 (Base URL & Endpoint)

*   **제공 기관**: 대한민국 기상청 (KMA)
*   **인증 및 보안**: 개인 인증키 (공공데이터포털 발급 마스터 API Key)
*   **프로토콜**: RESTful GET HTTPS
*   **엔드포인트**:
    *   *자외선지수 조회 (UV Index)*: `https://apis.data.go.kr/1360000/LivingWthrIdxServiceV4/getUVIdxV4`
    *   *체감온도지수 조회 (Sensory Temp)*: `https://apis.data.go.kr/1360000/LivingWthrIdxServiceV4/getSenTaIdxV4`

---

## 📥 2. 요청 파라미터 규격 (Request Parameters)

엔노이아 API 커넥터 설정 화면의 `Parameters` 탭에 등록해야 할 규격입니다. `areaNo`와 `time`은 에이전트가 사용자의 위치 정보와 현재 시각을 파싱하여 동적으로 밀어 넣도록 변수 처리합니다.

| Parameter Name | Data Type | Requirement | Sample Value | Description (ennoia Variable Mapping) |
| :--- | :---: | :---: | :---: | :--- |
| `serviceKey` | String | 필수 (Required) | `6ab6edbe...` | 공공데이터포털에서 발급받은 **디코딩된 마스터 키** 직접 입력 |
| `dataType` | String | 필수 (Required) | `JSON` | 응답 포맷을 항상 JSON으로 설정하여 LLM 파싱 안정성 확보 |
| `areaNo` | String | 필수 (Required) | `1111000000` | 행정구역코드 10자리.<br>• 서울 종로구 기본값: **`${target_area_code}`** (기본값: `1111000000`) |
| `time` | String | 필수 (Required) | `2026060118` | 조회 년월일시 10자리 (YYYYMMDDHH).<br>• 기본값: **`${current_datetime_10}`** (실시간 기상 호출용) |
| `numOfRows` | Integer | 선택 (Optional) | `10` | 한 페이지 결과 수 |
| `pageNo` | Integer | 선택 (Optional) | `1` | 페이지 번호 |

> [!TIP]
> **엔노이아 가변수 `${target_area_code}` 매핑 가이드**:
> 사용자가 "종로구"를 언급하면, [Classify] 노드 또는 [의도 분류기]가 이를 인식하여 기상청 행정구역코드 `1111000000`으로 변환해 `${target_area_code}`에 주입하도록 설계합니다.

---

## 📤 3. 응답 데이터 규격 (Response JSON Sample & Mapping)

기상청 서버에서 반환하는 성공적인 JSON 응답 구조 예시입니다.

```json
{
  "response": {
    "header": {
      "resultCode": "00",
      "resultMsg": "NORMAL_SERVICE"
    },
    "body": {
      "dataType": "JSON",
      "items": {
        "item": [
          {
            "code": "A07",
            "areaNo": "1111000000",
            "date": "2026060118",
            "h0": "3",
            "h3": "3",
            "h6": "2",
            "h9": "0",
            "h12": "0",
            "h15": "0",
            "h18": "0",
            "h21": "0",
            "h24": "0"
          }
        ]
      },
      "numOfRows": 10,
      "pageNo": 1,
      "totalCount": 1
    }
  }
}
```

### 📊 주요 파서 변수 설명 (Response Fields)
*   `h0`: 발표 시각(현재) 기준 지수값. (예: `3`은 자외선지수 보통 단계를 의미)
*   `h3`, `h6`: 각각 3시간 뒤, 6시간 뒤의 예측 지수값. (2박 3일 일정을 조율할 때 사용)

---

## 🧠 4. 보행 약자 안전 판단 기준 테이블 (Safety Evaluation Logic)

에이전트는 API 응답 데이터(`h0` 값)를 읽고 다음과 같은 기상 안전 임계치를 스스로 평가하여 추천 일정을 보정합니다.

### ☀️ A. 자외선지수 (UV Index) 임계치 행동 요령
*   **0 ~ 2 (낮음)**: 야외 활동에 제약 없음. 광화문광장, 청계천 산책 추천 가능.
*   **3 ~ 5 (보통)**: 2~3시간 야외 보행 시 모자, 선글라스, 자외선 차단제 필수 안내.
*   **6 ~ 7 (높음) [⚠️ 주의 단계]**:
    *   *행동 규칙*: 오전 11시 ~ 오후 3시 사이 보행 약자의 야외 이동을 최소화하고, 그늘이 없는 코스는 제외.
    *   *에이전트 조치*: 해당 시간대 일정을 **MMCA 미술관, 세종이야기 등 100% 무단차 실내 전시관 관람**으로 자동 전환.
*   **8 ~ 10 (매우 높음) / 11 이상 (위험) [🚨 비상 단계]**:
    *   *행동 규칙*: 보행 약자의 낮 시간대 야외 활동 전면 금지.
    *   *에이전트 조치*: 청계천 도보길, 경복궁 야외 마당 코스를 전면 삭제하고, **서울공예박물관 실내 동선 및 차량 이동 동선**으로 강제 우회 처방.

### 🌡️ B. 체감온도지수 (Sensory Temp) 임계치 행동 요령
*   **32°C 이상 (경고 - 폭염 수준) [⚠️ 고령자 열사병 위험]**:
    *   *행동 규칙*: 고령의 실버 관광객은 야외에서 15분 이상 지속 보행 불가. 휠체어 이용자는 지면 반사열에 취약하므로 주의 필요.
    *   *에이전트 조치*: 일정 중간마다 반드시 **'안녕인사동', '광화문 D타워' 등 냉방과 휴게 쉼터가 완비된 복합몰 휴식 시간(최소 1시간)**을 억지로 끼워 넣도록 동선 강제 재구성.
