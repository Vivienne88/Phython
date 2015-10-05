import sys

try :
    import xlsxwriter

    def search(count,flag,T,fp) :    
        for i in fp :
            #파싱
            c = i.strip().split("|",4)#초기화
            if count==0 :
                   T[count-1]=c[2]
                   T.append(None)
                   count+=1
            else :
                   #중복확인
                   for j in range(0,count) :
                       #하나라도 다르면
                       if T[j]==c[2] :
                           flag=1       
                           break
                       #모두 다르면
                       if j==count-1 :
                           flag=0
           
                   #중복이 없을 경우에만 대입
                   if not flag==1 :
                           T[count]=c[2]
                           T.append(None)
                           count+=1
                           flag=0
        return T      

    def m_print(T) :
        print("===3번 목록===")
        for i in T :
            if i != None :
                print(i)

    def make_excel(word,fp,count) :
        #엑셀 생성
        workbook = xlsxwriter.Workbook(word+'.xlsx')
        worksheet = workbook.add_worksheet()
        
        for i in fp :
            #파싱
            c = i.strip().split("|",4)
            #찾았을 경우
            if c[2].find(word)!=-1 :
                #출력
                for j in range(4) :        
                    worksheet.write(chr(ord('A')+j)+str(count), c[j])
                count+=1
        #완료 알림
        print(word+".xlsx 저장이 완료되었습니다.")
        return workbook

    #txt 파일 로드
    fp = open("201401.txt","r")

    #초기화
    count=0
    flag=0
    T=[None]

    #중복 확인
    T=search(count,flag,T,fp)
                          
    #출력 함수
    m_print(T)
 
    #입력
    word=input("찾고 싶은 단어를 입력하세요 : ")

    #초기화
    count=1
    fp.seek(0)

    #엑셀 생성 및 검색
    workbook = make_excel(word,fp,count)

    #닫기
    fp.close()
    workbook.close()

except :
    error = sys.exc_info()
    print(error[2])