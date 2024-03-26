import csv, datetime, os
import ImageRecognition.CalculateSimilarity as cal_sim
from ImageRecognition.MenuModel import Model

def create_csv(model: Model):
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    with open("ImageRecognition\output\similarity_" + now + ".csv", "w") as file:
        writer = csv.writer(file)
        
        header_list = ['ファイル名１', 'ファイル名2', 'ヒストグラム比較結果', 'SSIM比較結果']
        writer.writerow(header_list)
        
        for image1_path, image2_path in zip(model.get_image1_file_paths(), model.get_image2_file_paths()):
            output_list = []
            output_list.append(os.path.basename(image1_path))
            output_list.append(os.path.basename(image2_path))
            output_list.append(cal_sim.calculate_histogram_similarity(image1_path, image2_path))
            output_list.append(cal_sim.calculate_ssim(image1_path, image2_path))
            
            writer.writerow(output_list)
            
        print("CSVファイルへの書き込みが終了しました")