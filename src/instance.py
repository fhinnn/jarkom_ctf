import json
import random
import string

def generate_random_flags(num_flags=1, random_string_length=20):
    prefix = "Jarkom2023{th1s_i5_ur_fl4g_"
    suffix = "}"
    
    for _ in range(num_flags):
        uppercase_part = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
        lowercase_part = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        numeric_part = ''.join(random.choice(string.digits) for _ in range(6))
        
        alphanumeric_part = uppercase_part + lowercase_part + numeric_part
        alphanumeric_list = list(alphanumeric_part)
        random.shuffle(alphanumeric_list)
        shuffled_alphanumeric = ''.join(alphanumeric_list)
        
        flag = "{}{}{}".format(prefix, shuffled_alphanumeric, suffix)
    
    return flag


def main():
    try:
        input_json = input("Enter a JSON-formatted line: ")
        parsed_json = json.loads(input_json)
        
        if "challcode" in parsed_json and "answer" in parsed_json:
            challcode = parsed_json["challcode"]
            answer = parsed_json["answer"]
            print("Challenge Code:", challcode)
            print("Answer:", answer)
            
            with open("/home/ctf/answer.json", "r") as answer_file:
                correct_answers = json.load(answer_file)
            
            correct_answer = next((item["answer"] for item in correct_answers if item["challcode"] == challcode), None)
            
            if correct_answer is not None and correct_answer == answer:
                print("Correct answer!")
                #with open("flag.txt", "r") as flag_file:
                #    flags = flag_file.read().splitlines()
                random_flag = generate_random_flags()
                print("Flag:", random_flag)
            else:
                print("Incorrect answer or challenge code.")

        else:
            print("JSON must contain 'challcode' and 'answer' keys.")

    except json.JSONDecodeError:
        print("Invalid JSON format.")

if __name__ == "__main__":
    main()
