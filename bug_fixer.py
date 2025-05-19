from google.cloud import pubsub_v1, firestore
import time
import json

# Initialize Firestore and Subscriber
db = firestore.Client()
subscriber = pubsub_v1.SubscriberClient()

# Replace with your actual subscription path
subscription_path = subscriber.subscription_path('bugsquash-uniqueid', 'bug-fix-sub')

def callback(message):
    print(f"Received message: {message.data}")
    data = json.loads(message.data.decode("utf-8"))
    
    # Dummy bug fixing logic
    fixed_code = data["code"].replace("bug", "fix")
    
    # Store in Firestore
    db.collection("bugfixes").add({
        "original_code": data["code"],
        "fixed_code": fixed_code,
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    
    print("Bug fixed and stored in Firestore.")
    message.ack()

# Listen for messages
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}...\n")

try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
