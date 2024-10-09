
import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""
if __name__=="__main__":
    print(get_str_from_food_dict({"samosa":2, "chole":5}))
    # print(extract_session_id("projects/foodiebot-xmju/locations/global/agent/sessions/0d79fd47-722d-507d-0170-9e2c52537f55/contexts/ongoing-order"))