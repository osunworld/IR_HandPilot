import torch

# 현재 설정된 Conda 환경 이름 출력
import os
conda_env = os.environ.get('CONDA_DEFAULT_ENV')
print(f"현재 활성화된 Conda 환경: {conda_env}")

# PyTorch 버전 확인
print(f"PyTorch 버전: {torch.__version__}")

# GPU 사용 가능 여부 확인
if torch.cuda.is_available():
    print("GPU를 사용할 수 있습니다.")
    # 현재 사용 중인 GPU 장치 이름 출력
    print(f"GPU 장치 이름: {torch.cuda.get_device_name(0)}")
else:
    print("GPU를 사용할 수 없습니다.")
