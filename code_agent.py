from google.cloud import pubsub_v1
import json

PROJECT_ID = "bugsquash-uniqueid"
TOPIC_ID = "bug-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def publish_code_for_testing(code_snippet):
    message_json = json.dumps({"code": code_snippet})
    message_bytes = message_json.encode("utf-8")

    future = publisher.publish(topic_path, data=message_bytes)
    print(f"Published message ID: {future.result()}")

if __name__ == "__main__":
    print("Enter the code snippet you want to fix. End with an empty line:")
    user_code_lines = []
    while True:
        line = input()
        if line == "":
            break
        user_code_lines.append(line)
    user_code = "\n".join(user_code_lines)

    publish_code_for_testing(user_code)
