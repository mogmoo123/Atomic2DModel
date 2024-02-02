# Atomic2DModel
Bohr Atmoic Model in Python

# 원리
## 전자 채우는 원리
전자 껍질을 원 모양의 그래프라고 생각하고, 원자핵을 원점으로 둔 뒤, 전자가 있을 자리의 좌표를 **(x,y)** 로 정합니다.
보어의 원자모형에서 **전자는 2개 8개 8개 18개 18개 32개 32개 순서**로 전자 껍질을 채우고, 각각 360/2 = 180°, 360/8 = 45°, 45°, 360/18 = 20°, 20°, 360/32 = 11.25°, 11.25° 의 각도를 간격으로 채우므로
이 각도를 라디안값인 θ로 두고, x좌표와 y좌표를 θ와 전자 껍질의 반지름 r을 이용해 나타내면 **x=r*sin(θ) y=r*cos(θ)** 가 됩니다. 그후 (x,y) 좌표에 전자를 그립니다.
이를 각 원자 껍질의 원자 갯수만큼씩 반복해서 각각의 원자 껍질을 하나하나씩 채워가며 전자를 모두 채웁니다.

# 주기율표
주기율표의 csv파일은 PubChem에서 가져 왔습니다.
[PubChem](https://pubchem.ncbi.nlm.nih.gov/periodic-table/)

# 코드
변수 n : 원자번호
함수 Atomic : 보어의 원자 모형 그리기

# 추가사항
- tkinter을 활용한 GUI
- 이미지 저장기능
- 원소의 모형 뿐만 아니라 더 자세한 사항들을 출력할 수 있도록 만들 예정 (전기 음성도, 산화수, 이름, 상온에서의 상태 ...)

# 패치노트
