from report_insured import ReportInsured

def main():
    input_file = r'C:\work\source\testdata\社労夢データ.xlsx'
    template = r'C:\work\source\testdata\template.xlsx'
    template_copy = r'C:\work\source\testdata'
    # template_copy = r'C:\work\source\testdata\template_copy.xlsx'

    report_instance = ReportInsured()
    report_instance.generate(input_file, template, template_copy)

if __name__ == '__main__':
    main()