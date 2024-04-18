from django.shortcuts import render

# Create your views here.
def market(request):
    title = "스파르타 마켓 :: 마켓 플레이스"
    profile1 = "대표이사 : 이범규  "
    profile2 = "사업자등록번호 : 783-86-01715   |   통신판매업신고 : 2020-서울강남-02300  "
    profile3 = "호스팅서비스 제공자 :   "
    profile4 = "EMAIL : contact@teamsparta.co   |   TEL : 1522-8016" 
    profile5 = "주소 : 서울특별시 강남구 테헤란로44길 8 12층"
    return render(request, 'products.html', {'title':title,'profile1':profile1,'profile2':profile2,'profile3':profile3,'profile4':profile4,'profile5':profile5,})