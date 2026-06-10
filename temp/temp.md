# 🎨 크리넥스(Kleenex) 앱 로고 이미지 생성 프롬프트 가이드

웹 제미나이(Web Gemini) 또는 이미지 생성 모델(Imagen 3, DALL-E 3 등)에 그대로 복사해서 입력하실 수 있는 모바일 앱 로고/아이콘 생성용 고품질 프롬프트 모음입니다.

서비스의 핵심 정체성인 **'뽀송뽀송함(구름, 파스텔)'**과 **'보행 약자(휠체어, 경로)'**의 요소를 시각적으로 융합하여 프리미엄하게 디자인되었습니다.

---

## 🎨 옵션 A: 트렌디한 3D 클레이 스타일 (추천)
> 요즘 모바일 앱 트렌드인 몽글몽글하고 프리미엄한 3D 느낌의 큐트 아이콘 스타일입니다.

### 📋 복사용 영어 프롬프트 (English Prompt)
```text
A cute 3D clay-rendered mobile app icon featuring a fluffy white cloud shaped like a wheelchair, traveling along a smooth pastel-colored road. Warm and friendly tone, aesthetic pastel mint and baby blue gradient background, soft lighting, minimalist design, premium quality, isometric view, app logo style, 8k resolution.
```

### 🇰🇷 한글 프롬프트 (Korean Prompt)
```text
부드러운 흰색 구름이 휠체어 형태로 조각되어 평탄하고 부드러운 파스텔톤 길을 따라 여행하고 있는 귀여운 3D 클레이 스타일의 모바일 앱 아이콘. 따뜻하고 친근한 분위기, 파스텔 민트와 베이비 블루 그라데이션 배경, 부드러운 광원 효과, 미니멀리즘 디자인, 고품질, 입체적인 뷰, 앱 로고 스타일.
```

---

## 🎨 옵션 B: 미니멀 벡터 플랫 스타일
> 깔끔하고 정돈된 2D 그래픽 디자인 스타일로, 가독성이 높고 단정한 느낌을 줍니다.

### 📋 복사용 영어 프롬프트 (English Prompt)
```text
A minimalist 2D vector app icon of a friendly pastel-colored cloud embracing a golden wheelchair wheel, clean safety path, pastel blue and warm white color palette, flat design, simple shape, aesthetic, rounded corners, professional app logo design, solid background.
```

### 🇰🇷 한글 프롬프트 (Korean Prompt)
```text
친근한 파스텔톤 구름이 황금빛 휠체어 바퀴를 부드럽게 감싸 안고 있는 형태의 미니멀한 2D 벡터 앱 아이콘. 깨끗하고 안전한 도로 경로 융합, 파스텔 블루와 따뜻한 화이트 색상 팔레트, 플랫 디자인, 심플한 도형 구조, 세련됨, 둥근 모서리, 전문적인 앱 로고 디자인.
```

---

## 💡 웹 제미나이 사용 팁 (Gemini Usage Tips)
1. **영어 프롬프트**를 사용하시는 것이 고화질 로고 이미지 생성에 훨씬 정밀하고 아름다운 결과물을 보여줍니다.
2. 원하는 느낌에 가까운 결과물이 나왔을 때, 마우스 우클릭으로 저장하시거나 제미나이의 다운로드 기능을 이용해 PPTX 템플릿(Slide 1 또는 데모 화면 내부)의 로고 위치에 배치하시면 됩니다.

---

## 💡 피그마(Figma) 가져오기 시 이미지 누락 해결 가이드 (옵시디언 뷰어)
로컬 HTML 파일을 `html.to.design` 플러그인으로 피그마에 가져올 때 브라우저 보안 제한으로 인해 이미지가 빈 흰색 상자로 보일 수 있습니다. 아래 캡처본들을 참조하여 피그마의 빈 상자 영역에 드래그 앤 드롭으로 채워주세요.

### 1. 슬라이드 1 (표지) - 오른쪽 로고 프레임
*   **파일명:** `kleenex_app_logo.jpeg`
*   ![크리넥스 앱 로고](contest_materials/reference/kleenex_app_logo.jpeg)

### 2. 슬라이드 2 (문제 정의) - 오른쪽 캐릭터 일러스트
*   **파일명:** `accessibility_obstacle.png`
*   ![휠체어 극복 3D 캐릭터](contest_materials/reference/accessibility_obstacle.png)

### 3. 슬라이드 3 (핵심 아키텍처) - 오른쪽 오케스트레이션 맵
*   **파일명:** `orchestration_canvas.png`
*   ![엔노이아 캔버스 설계도](contest_materials/reference/orchestration_canvas.png)

### 4. 슬라이드 4 (OpenAPI 명세) - 오른쪽 아래 첫 번째 상자
*   **파일명:** `api_spec_raw.png`
*   ![공공데이터 명세 캡처](contest_materials/reference/api_spec_raw.png)

### 5. 슬라이드 4 (OpenAPI 명세) - 오른쪽 아래 두 번째 상자
*   **파일명:** `connector_add.png`
*   ![엔노이아 API 커넥터 추가 설정 화면](contest_materials/reference/connector_add.png)

### 6. 슬라이드 7 (시나리오 A - 날씨 보통) - 왼쪽 위 첫 번째 상자
*   **파일명:** `normal_scenario_qa.png`
*   ![일반 시나리오 챗봇 대화창](contest_materials/reference/normal_scenario_qa.png)

### 7. 슬라이드 7 (시나리오 A - 날씨 보통) - 왼쪽 위 두 번째 상자
*   **파일명:** `bf_safety_criteria_qa.png`
*   ![무장애 기준 정합성 검증 대화창](contest_materials/reference/bf_safety_criteria_qa.png)

### 8. 슬라이드 7 (시나리오 A - 날씨 보통) - 아래쪽 가로로 긴 상자
*   **파일명:** `user_approval_ui.png`
*   ![사용자 직접 승인 팝업 UI](contest_materials/reference/user_approval_ui.png)

### 9. 슬라이드 8 (시나리오 B - 날씨 경보) - 오른쪽 큰 상자
*   **파일명:** `weather_caution_qa.png`
*   ![기상 악화 시 실내 스왑 우회 챗봇 대화창](contest_materials/reference/weather_caution_qa.png)

### 10. 슬라이드 9 (비즈니스 가치) - 오른쪽 스마트폰 3D 목업
*   **파일명:** `kakao_export_mockup.png`
*   ![알림톡 전송 완료 3D 캐릭터 목업](contest_materials/reference/kakao_export_mockup.png)


