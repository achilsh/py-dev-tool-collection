import basic_demo

def main():
    print("Hello from demo-uv-pkg!")
    d = basic_demo.Demo(100) 
    print(f"data1: {d.get()}")
    d.call(200)
    print(f"data2: {d.get()}")

# 
    # basic_demo.call_pandas()

if __name__ == "__main__":
    main()
