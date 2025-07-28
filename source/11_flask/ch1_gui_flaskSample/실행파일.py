from predict import loaded_model, predict_apt_price
import xlwings as xw

def main():
    '엑셀파일 열고, 데이터 가져와 예측한 결과 저장하기'
    file_path = "../data/ex3_xlwing.xlsx"
    wb = xw.Book(file_path)
    ws = wb.sheets.active
    # 엑셀 데이터를 읽어 예측하고 E열에 결과 넣기
    for line in range(2,5):
        year = ws.range('b'+str(line)).value
        square = ws.range('c'+str(line)).value
        floor = ws.range('d'+str(line)).value
        pred = predict_apt_price(year, square, floor)
        ws.range('e'+str(line)).value = pred
    wb.save(file_path)
    wb.close()

if __name__=="__main__":
    main()