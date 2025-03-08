def sandwich(*items):
    print(f"\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

sandwich('cabbage')
sandwich('cabbage', 'tomato', 'celery')
sandwich('celery', 'carrot', 'onion', 'corn', 'beans', 'capsicum')
