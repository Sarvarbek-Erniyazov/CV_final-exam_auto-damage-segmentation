# Auto Damage Segmentation — Hisobot

## Muammo
Avtomobil qismlarini avtomatik aniqlash va segmentatsiya qilish.
Sug'urta kompaniyalari va ta'mirlash markazlari uchun shikastlangan qismlarni tezkor aniqlash tizimi.

## Yechim
YOLOv8-seg modeli asosida instance segmentation pipeline yaratildi.

## Dataset
- Manba: Roboflow Universe (Car Parts Segmentation)
- Asl rasmlar: 603
- Augmentatsiyadan keyin: 1503
- Classlar soni: 19
- Train/Val/Test: 1350 / 75 / 78

## Model
- Arxitektura: YOLOv8n-seg
- Epochs: 50
- Image size: 640x640
- Export: ONNX (12.7 MB)

## Metrikalar
- mAP50: ~0.73
- Mask mAP50: ~0.73
- Precision: ~0.66
- Recall: ~0.79

## Demo Natijalari
| Rasm | Aniqlangan qismlar |
|------|-------------------|
| Rasm 1 (ezilgan mashina) | 8 ta qism |
| Rasm 2 (daraxt ostida) | 4 ta qism |
| Rasm 3 (kuchli zarar) | 9 ta qism |

## Deployment
- Roboflow: dataset va versiya boshqaruvi
- FastAPI: /predict endpoint (lokal)
- ONNX: cross-platform inference
