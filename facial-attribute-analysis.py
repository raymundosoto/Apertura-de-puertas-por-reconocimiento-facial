from deepface import DeepFace

obj = DeepFace.analyze (img_path = "/home/raymundo/Documents/apertura-puertas-reconocimiento-facial/image.jpeg", actions = ['age', 'gender', 'race', 'emotion'])

print ("El resultado del analisis es: ")
print (obj)
