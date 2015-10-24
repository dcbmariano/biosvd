#     Program: sort.py
#    Function: ordena resultados
# Description: eh incluido por biosvd.py
#      Author: Thiago da Silva Correia, Diego Mariano, Jose Renato Barroso, Raquel de Melo-Minardi
#     Version: 3


from Bio import SeqIO
class Sort(object):
	
	def __init__(self, nameFileModelo, nameFileModeloFamilia ):
		FileModelo = open(nameFileModelo, 'rU')
		FileModeloFamilia = open(nameFileModeloFamilia, 'rU')
		FilseqModeloOrdenadas = open("tmp/SeqModeloAgrupadas.fasta", 'w')
		self.FamiliasModelo=[]
		self.distribuicaoFamiliasModelos = []

		print "sort.py: parsing"
		# Aqui faremos um PARSE dos arquivos .fasta para obter as sequencias a serem trabalhas
		sequenciasModelo = list(SeqIO.parse(FileModelo, "fasta"))

		FileModelo.close()

		seqs = []
		Todasfamilias = [] # Familias
		FamiliaNaOrdem = [] #Ordem com que as familias aparecem no arquivo. (Com repeticao )

		#Modelo
		Aux = FileModeloFamilia.readline()
		Aux = FileModeloFamilia.readline()
		while ( Aux ):
			temp = Aux.split('\t')
			tempA = temp[7].split(',')
			i = tempA[0].rstrip().find("Glycosyl hydrolase")
			# Faco a busca apartir da posicao em que se encotra o Glycosyl hydrolase
			j = tempA[0].rstrip().find("family",i, len(tempA[0].rstrip()))
			family = tempA[0].rstrip()[i:j-1]
			if(len(family)>0):
				FamiliaNaOrdem.append( family )
				if family not in Todasfamilias:
					Todasfamilias.append(family)
			Aux = FileModeloFamilia.readline()
		#if tempA[0].rstrip() not in Todasfamilias:
		#	Todasfamilias.append(tempA[0].rstrip())
	
	
		#Gravando o numero total de familas do Modelo
		FilseqModeloOrdenadas.write(str(len(Todasfamilias))+'\n')
		k = 0
		for fam in Todasfamilias:
			FilseqModeloOrdenadas.write(str(fam)+'\n')
			for i in range(len(FamiliaNaOrdem)):
				if fam == FamiliaNaOrdem[i]:
					k = k+1
					seqs.append(i)
			#SeqIO.write( sequenciasModelo[i], FilseqOrdenadas, "fasta")
			FilseqModeloOrdenadas.write(str(k)+'\n')
		#print k

		#gravando as sequenciasModelo no arquivo
		for i in seqs:
			SeqIO.write( sequenciasModelo[i], FilseqModeloOrdenadas, "fasta")

		del FamiliaNaOrdem[:]
		del Todasfamilias[:]
		del seqs[:]
		FileModeloFamilia.close()
		FilseqModeloOrdenadas.close()