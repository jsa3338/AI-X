import datetime
from naverOpenai import get_naver_api_data, str_json_dataframe
import xlwings as xw
import shutil

def handle_init_sheet(file_path, wb):
    # 2~4
    # 2. 백업 (파일명 : genai_rap25071125852.xls)
    timestamp = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    backupfile = f"genai_rpa{timestamp}"
    shutil.copy(file_path, backupfile)
    print('백업파일 생성완료:', backupfile)

    # 3. 'prev_list' 시트를 삭제
    sheet_names = [s.name for s in wb.sheets]
    if 'prev_list' in sheet_names:
        wb.sheets['prev_list'].delete()
        print('prev_list 시트 삭제 완료')
    else:
        print('prev_list 시트가 존재하지 않아 삭제 못함')

    # 4. 'now_list'시트를 복사하여 'prev_list'시트로 시트 이름 변경
    if 'now_list' in sheet_names:
        now_sheet = wb.sheets['now_list']
        prev_sheet = now_sheet.copy(after=now_sheet)
        prev_sheet.name = 'prev_list'
        print('now_list 시트 prev_list시트로 복사 완료')
    else:
        print('now_list 시트가 존재하지 않아 작업 중단')
        return

def update_now_list(wb, df_shopping):
    # 6. 'now_list'시트의 모든 내용을 클리어하고, df_shopping내용('A1'셀)을 업데이트
    now_sheet = wb.sheets['now_list']
    now_sheet.clear()
    now_sheet.range('A1').value = df_shopping
    print("now_list 내용 업데이트 완료")

def save_close_file(file_path, wb):
    # 7. 파일 저장 및 닫기
    wb.save(file_path)
    wb.close()
    print('workbook 저장 완료')

def update_now_report(wb, analysis, summary):
    sheet_names = [s.name for s in wb.sheets]
    if 'prev_report' in sheet_names:
        wb.sheets['prev_report'].delete()
        print('prev_report 시트 삭제 완료')
    else:
        print('prev_report 시트 존재하지 않아 삭제 못함')
    
    if 'now_report' in sheet_names:
        now_sheet = wb.sheets['now_report']
        prev_report = now_sheet.copy(after=now_sheet)
        prev_report.name = 'prev_report'
        print('prev_report 시트 복사 완료')
    else:
        print('now_report 시트가 없어서 작업을 중단합니다.')
        wb.close()
        return
    # 분석글(analysis, summary)을 now_report 시트에 업데이트
    current_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 시간은 A3 셀에 입력
    now_sheet.range('A3').value = current_dt+" 기준" # 우측 정렬
    now_sheet.range('A3').api.HorizontalAlignment = xw.constants.HAlign.xlHAlignRight
    # now_sheet.range('A3').api.HorizontalAlignment = -4152
    # analysis는 A5셀에 입력
    now_sheet.range('A5').value = analysis
    now_sheet.range('A5').api.WrapText = True # 내용이 셀보다 길면 자동 줄바꿈 활성화

