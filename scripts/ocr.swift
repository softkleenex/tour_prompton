import Foundation
import Vision
import AppKit

guard CommandLine.arguments.count > 1 else {
    print("Usage: ocr <image-path>")
    exit(1)
}

let imagePath = CommandLine.arguments[1]
let url = URL(fileURLWithPath: imagePath)

guard let image = NSImage(contentsOf: url),
      let tiffData = image.tiffRepresentation,
      let ciImage = CIImage(data: tiffData) else {
    print("ERROR: Failed to load image at \(imagePath)")
    exit(1)
}

let requestHandler = VNImageRequestHandler(ciImage: ciImage, options: [:])

// Semaphore to wait for async OCR block to complete
let semaphore = DispatchSemaphore(value: 0)

let request = VNRecognizeTextRequest { (request, error) in
    defer { semaphore.signal() }
    
    if let error = error {
        print("ERROR: \(error.localizedDescription)")
        return
    }
    
    guard let observations = request.results as? [VNRecognizedTextObservation] else {
        return
    }
    
    for observation in observations {
        guard let candidate = observation.topCandidates(1).first else { continue }
        print(candidate.string)
    }
}

// Set recognition configuration
request.recognitionLanguages = ["ko-KR", "en-US"]
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true

do {
    try requestHandler.perform([request])
    semaphore.wait()
} catch {
    print("ERROR: Failed to perform recognition: \(error.localizedDescription)")
}
