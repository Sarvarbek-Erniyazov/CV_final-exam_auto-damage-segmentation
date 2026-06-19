# 🚗 Auto Damage Segmentation

Mashina qismlarini avtomatik aniqlash va segmentatsiya qilish tizimi.
Sug'urta va ta'mirlash markazlari uchun shikastlangan qismlarni tezkor aniqlash.

## 🔗 Links

| | Link |
|---|---|
| 🤗 Live Demo | [Hugging Face Space](https://huggingface.co/spaces/Sarvarbek13/auto-damage-segmentation) |
| 📦 Dataset | [Roboflow Car Parts](https://universe.roboflow.com/person-detector/car-parts-segmentation) |
| 💻 GitHub | [CV Final Exam Repo](https://github.com/Sarvarbek-Erniyazov/CV_final-exam_auto-damage-segmentation) |

## 🧠 Pipeline

Roboflow Dataset → YOLOv8-seg Fine-tuning → ONNX Export → YOLO + SAM → FastAPI + Gradio

## 📦 Texnologiyalar

- YOLOv8-seg — instance segmentation (fine-tuned)
- SAM — Segment Anything Model (Meta AI)
- FastAPI — lokal REST API
- Gradio — web demo (Hugging Face)
- ONNX — production deployment format
- Roboflow — dataset management

## 📁 Struktura

    auto-damage-segmentation/
    ├── api/
    │   ├── main.py
    │   └── requirements.txt
    ├── model/
    │   ├── best.pt
    │   └── best.onnx
    ├── notebook/
    │   └── train.ipynb
    ├── report/
    │   └── hisobot.md
    └── README.md

## 📊 Metrikalar

| Metrika | Qiymat |
|---------|--------|
| mAP50 | ~0.73 |
| Mask mAP50 | ~0.73 |
| Precision | ~0.66 |
| Recall | ~0.79 |
| Classes | 19 |
| Dataset | 1503 rasm |

## 🧪 Demo Natijalari (YOLO + SAM)

| Rasm | Detections | SAM Masks |
|------|-----------|-----------|
| Ezilgan mashina | 8 | 8 |
| Orqa zarar | 3 | 3 |
| Kuchli zarar | 8 | 8 |
