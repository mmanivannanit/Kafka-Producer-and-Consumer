from confluent_kafka import Producer

p = Producer({
    'bootstrap.servers': 'localhost:9921,localhost:9922,localhost:9923'
})
p.produce('tjson')


try:
    with open('/home/mani/Logs/output.json') as f:
        val = f.readlines()
        print(val)
        for m in val:
        
            print(m.split())
            p.produce('tjson', 
            key="{0}".format(val), value='myvalue #{0}'.format(m))
        p.poll(0.5)
except KeyboardInterrupt:
    pass

print("flushing...")
p.flush(30)
print("done")
