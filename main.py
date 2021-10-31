import os
import argparse
import json
import lib 
import lib.predict as pred   

def save_task3_json(task_num, set_num, pred_data, file_path=None):
    data, data_chk = {}, {}
    indent = 3
    
    if os.path.isfile(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file) 
        indent += 1
    else:
        data[f"{task_num}"] = []
    
    data[f"{task_num}"].append({f"{set_num}": pred_data})

    with open(file_path, 'w') as json_file: 
        json.dump(data, json_file, indent=indent)
    with open(file_path, 'r') as json_file: 
        data_chk = json.load(json_file)
    print("{0} updated... > {1}".format(file_path, "OK" if data == data_chk else "Failed"))


def main(args):
    if os.path.exists(args.json_path) == True:
        os.remove(args.json_path)
    n_set = 5 if args.set_num == "all_sets" else 1
        
    for i in range(n_set):
        args.set_num = f"set_0" + str(i+1) if n_set == 5 else args.set_num
        print("count : ", args.set_num)

        # task_1
        # todo

        # task_2
        # todo

        # task_3
        t3_data = []
        t3 = pred.func_task3(args)
        t3_res_pred_move, t3_res_pred_stay, t3_res_pred_total = t3.run()
        t3_data.append(t3_res_pred_move)
        t3_data.append(t3_res_pred_stay)
        t3_data.append(t3_res_pred_total)

        # save result to json file
        save_task3_json(task_num="task3_answer", set_num=args.set_num, pred_data=t3_data, file_path=args.json_path)

        # task_4
        # todo

        

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    # path
    # p.add_argument("--dataset_dir", type=str, default="/home/agc2021/dataset") # /set_01, /set_02, /set_03, /set_04, /set_05
    # p.add_argument("--root_dir", type=str, default="/home/[Team_ID]")
    # p.add_argument("--temporary_dir", type=str, default="/home/agc2021/temp")
    ###
    p.add_argument("--dataset_dir", type=str, default="../dataset") # /set_01, /set_02, /set_03, /set_04, /set_05
    p.add_argument("--root_dir", type=str, default=".")
    p.add_argument("--temporary_dir", type=str, default="../temp")
    ###
    p.add_argument("--json_path", type=str, default="answersheet_3_00_mlvlab.json")
    p.add_argument("--task_num", type=str, default="task3_answer")
    p.add_argument("--set_num", type=str, default="all_sets") 
    p.add_argument("--device", default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')

    args = p.parse_args()

    main(args)

    

