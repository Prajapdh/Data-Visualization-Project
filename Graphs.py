
ax=plt.axes()

def Bugbar():
    Bug=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Bug["Name"]
    HPi=Bug["HP"]
    Attacki=Bug["Attack"]
    Defensei=Bug["Defense"]
    plt.xlabel("Name of pokemon")
    

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one stackbar chart")
    print("press 5 to merge all the data in one multibar chart")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        bugbar=ax.set_facecolor("navajowhite")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.bar(Namei,HPi)
        plt.xticks(rotation="vertical")
        plt.show()

    elif pt==2:
        bugbar=ax.set_facecolor("bisque")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.bar(Namei,Attacki,color="r")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==3:
        bugbar=ax.set_facecolor("lightpink")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.bar(Namei,Defensei,color="m")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==4:
        bugbar=ax.set_facecolor("peachpuff")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs all abilities")
        plt.bar(Namei,HPi,width=0.2,label="Name Vs HP")
        plt.bar(Namei,Attacki,width=0.2,label="Name Vs Attack strength")
        plt.bar(Namei,Defensei,width=0.2,label="Name Vs defense strength")
        plt.xticks(rotation="vertical")
        plt.legend()
        plt.show()

    elif pt==5:
        bugbar=ax.set_facecolor("peachpuff")
        VD=np.arange(len(Namei))
        plt.bar(VD,HPi,width=0.33,label="Name Vs HP")
        plt.bar(VD+0.33,Attacki,width=0.33,label="Name Vs Attack strength")
        plt.bar(VD+0.66,Defensei,width=0.33,label="Name Vs defense strength")
        plt.xticks(VD,Namei,rotation="vertical")
        plt.title("Name Vs all abilities")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")      
        

def Bughistogram():
    Bug=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Totali=Bug["Total"]
    Bughisto=ax.set_facecolor("lightgoldenrodyellow")
    plt.hist(Totali,bins=[0,100,200,300,400,500,634],color="g")
    plt.ylabel("Total Number of different BUG pokemons")
    plt.title("Range wise total number of bug pokemons")
    plt.xticks(rotation="vertical")
    plt.show()


def Bugline():
    Bug=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Bug["Name"]
    HPi=Bug["HP"]
    Attacki=Bug["Attack"]
    Defensei=Bug["Defense"]
    plt.xlabel("Name of pokemon")
    plt.xticks(rotation="vertical")
    
    print("press 1 to print the data for POKEMON v/s HP")
    print("press 2 to print the data for POKEMON v/s ATTACK")
    print("press 3 to print the data for POKEMON v/s DEFENCE")
    print("press 4 to print the data for POKEMON v/s ALL ABILITIES")


    pt=int(input("Enter your choice="))

    if pt==1:
        bugline=ax.set_facecolor("steelblue")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.plot(Namei,HPi,color="w",marker='o',markersize=8,markeredgecolor='midnightblue',markerfacecolor="lavenderblush",linestyle="dashed",linewidth=2,label="NAME V/S HP")
        plt.show()

    elif pt==2:
        bugline=ax.set_facecolor("steelblue")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.plot(Namei,Attacki,color="w",marker='o',markersize=8,markeredgecolor='midnightblue',markerfacecolor="lavenderblush",linestyle="dashed",linewidth=2,label="NAME V/S HP")
        plt.show()
        
    elif pt==3:
        bugline=ax.set_facecolor("steelblue")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.plot(Namei,Defensei,color="w",marker='o',markersize=8,markeredgecolor='midnightblue',markerfacecolor="lavenderblush",linestyle="dashed",linewidth=2,label="NAME V/S HP")
        plt.show()

    elif pt==4:
        bugline=ax.set_facecolor("antiquewhite")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.plot(Namei,HPi,color="r",label="NAME V/S HP")
        plt.plot(Namei,Attacki,color="c",label="NAME V/S ATTACK")
        plt.plot(Namei,Defensei,color="m",label="NAME V/S DEFENSE")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")        


def Bugpie():
    Bug=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Bug["Name"]
    HPi=Bug["HP"]
    Attacki=Bug["Attack"]
    Defensei=Bug["Defense"]

    print("press 1 for the data for name of pokemon Vs HP of pokemons")
    print("press 2 for the data for name of pokemon Vs Attack strength of pokemons")
    print("press 3 for the data for name of pokemon Vs Defense strength of pokemons")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        plt.title("name vs HP")
        plt.pie(HPi,labels=Namei)
        #autopct attribute can be used to show the percentage of the data.
        plt.show()
        

    elif pt==2:
        plt.title("Name Vs Attack strength")
        plt.pie(Attacki,labels=Namei)
        plt.show()
        
    elif pt==3:
        plt.title("Name Vs defense strength")
        plt.pie(Defensei,labels=Namei)
        plt.show()
    
    else:
        print("enter vaid input")


def Bugscatter():
    Bug=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Bug["Name"]
    HPi=Bug["HP"]
    Attacki=Bug["Attack"]
    Defensei=Bug["Defense"]
    plt.xlabel("Name of pokemons")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one scatter chart")

    axs=plt.gca()
    
    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        bugscatter=ax.set_facecolor("lightsteelblue")
        plt.ylabel("HP of pokemons")
        axs.scatter(Namei,HPi,color="k")
        plt.title("Name vs HP")
        plt.show()
        
    elif pt==2:
        bugscatter=ax.set_facecolor("lightsteelblue")
        plt.ylabel("Attack strength of pokemons")
        axs.scatter(Namei,Attacki,color="royalblue")
        plt.title("Name vs Attack strength")
        plt.show()
        
    elif pt==3:
        bugscatter=ax.set_facecolor("lightsteelblue")
        plt.ylabel("Defense strength of pokemons")
        axs.scatter(Namei,Defensei,color="navy")
        plt.title("Name Vs defense strength")
        plt.show()

    elif pt==4:
        bugscatter=ax.set_facecolor("lightsteelblue")
        plt.ylabel("All abilities of pokemons")
        axs.scatter(Namei,HPi,color="k",label="Name Vs HP")
        axs.scatter(Namei,Attacki,color="royalblue",label="Name Vs Attack")
        axs.scatter(Namei,Defensei,color="navy",label="Name Vs Defense")
        plt.title("complete analysis of pokemons")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")   
 

def Darkbar():
    Dark=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Dark["Name"]
    HPi=Dark["HP"]
    Attacki=Dark["Attack"]
    Defensei=Dark["Defense"]
    plt.xlabel("Name of pokemon")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one stackbar chart")
    print("press 5 to merge all the data in one multibar chart")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        darkbar=ax.set_facecolor("navajowhite")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.bar(Namei,HPi)
        plt.xticks(rotation="vertical")
        plt.show()

    elif pt==2:
        darkbar=ax.set_facecolor("bisque")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.bar(Namei,Attacki,color="r")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==3:
        darkbar=ax.set_facecolor("lightpink")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.bar(Namei,Defensei,color="m")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==4:
        darkbar=ax.set_facecolor("peachpuff")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs all abilities")
        plt.bar(Namei,HPi,width=0.2,label="Name Vs HP")
        plt.bar(Namei,Attacki,width=0.2,label="Name Vs Attack strength")
        plt.bar(Namei,Defensei,width=0.2,label="Name Vs defense strength")
        plt.xticks(rotation="vertical")
        plt.legend()
        plt.show()

    elif pt==5:
        darkbar=ax.set_facecolor("peachpuff")
        VD=np.arange(len(Namei))
        plt.bar(VD,HPi,width=0.33,label="Name Vs HP")
        plt.bar(VD+0.33,Attacki,width=0.33,label="Name Vs Attack strength")
        plt.bar(VD+0.66,Defensei,width=0.33,label="Name Vs defense strength")
        plt.xticks(VD,Namei,rotation="vertical")
        plt.title("Name Vs all abilities")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")
       

def Darkhistogram():
    Dark=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Totali=Dark["Total"]
    ax=plt.axes()
    Darkhisto=ax.set_facecolor("paleturquoise")
    plt.hist(Totali,bins=[300,400,500,600],color="k")
    plt.ylabel("Total Number of different DARK pokemons")
    plt.title("Range wise total number of Dark pokemons")
    plt.xticks(rotation="vertical")
    plt.show()


def Darkline():
    Dark=pd.read_csv("D:\python projects\schoolproject\Dark.csv")
    Namei=Dark["Name"]
    HPi=Dark["HP"]
    Attacki=Dark["Attack"]
    Defensei=Dark["Defense"]
    plt.xlabel("Name of pokemon")
    plt.xticks(rotation="vertical")
    
    print("press 1 to print the data for POKEMON v/s HP")
    print("press 2 to print the data for POKEMON v/s ATTACK")
    print("press 3 to print the data for POKEMON v/s DEFENCE")
    print("press 4 to print the data for POKEMON v/s ALL ABILITIES")

    pt=int(input("Enter your choice="))

    if pt==1:
        Darkline=ax.set_facecolor("lightsteelblue")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.plot(Namei,HPi,color="k",marker='p',markersize=10,markeredgecolor='c',markerfacecolor="darkslategrey",linestyle="dashdot",linewidth=2,label="NAME V/S HP")
        plt.show()

    elif pt==2:
        Darkline=ax.set_facecolor("lightsteelblue")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.plot(Namei,Attacki,color="k",marker="p",markersize=10,markeredgecolor='c',markerfacecolor="darkslategrey",linestyle="dashdot",linewidth=2,label="NAME V/S ATTACK")
        plt.show()
        
    elif pt==3:
        Darkline=ax.set_facecolor("lightsteelblue")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.plot(Namei,Defensei,color="k",marker="p",markersize=10,markeredgecolor='c',markerfacecolor="darkslategrey",linestyle="dashdot",linewidth=2,label="NAME V/S DEFENSE")
        plt.show()

    elif pt==4:
        Darkline=ax.set_facecolor("linen")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.plot(Namei,HPi,color="b",label="NAME V/S HP")
        plt.plot(Namei,Attacki,color="g",label="NAME V/S ATTACK")
        plt.plot(Namei,Defensei,color="m",label="NAME V/S DEFENSE")
        plt.legend()
        plt.show()

    else:
        print("enter valid input") 


def Darkpie():
    Dark=pd.read_csv("D:\python projects\schoolproject\Dark.csv")
    Namei=Dark["Name"]
    HPi=Dark["HP"]
    Attacki=Dark["Attack"]
    Defensei=Dark["Defense"]

    print("press 1 for the data for name of pokemon Vs HP of pokemons")
    print("press 2 for the data for name of pokemon Vs Attack strength of pokemons")
    print("press 3 for the data for name of pokemon Vs Defense strength of pokemons")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        plt.title("name vs HP")
        plt.pie(HPi,labels=Namei)
        #autopct attribute can be used to show the percentage of the data.
        plt.show()
        

    elif pt==2:
        plt.title("Name Vs Attack strength")
        plt.pie(Attacki,labels=Namei)
        plt.show()
        
    elif pt==3:
        plt.title("Name Vs defense strength")
        plt.pie(Defensei,labels=Namei)
        plt.show()
    
    else:
        print("enter vaid input")


def Darkscatter():
    Dark=pd.read_csv("D:\python projects\schoolproject\Dark.csv")
    Namei=Dark["Name"]
    HPi=Dark["HP"]
    Attacki=Dark["Attack"]
    Defensei=Dark["Defense"]
    plt.xlabel("Name of pokemons")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one scatter chart")

    axs=plt.gca()
    
    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        Darkscatter=ax.set_facecolor("lightsteelblue")
        plt.ylabel("HP of pokemons")
        axs.scatter(Namei,HPi,color="brown")
        plt.title("Name vs HP")
        plt.show()
        
    elif pt==2:
        Darkscatter=ax.set_facecolor("lightsteelblue")
        plt.ylabel("Attack strength of pokemons")
        axs.scatter(Namei,Attacki,color="k")
        plt.title("Name vs Attack strength")
        plt.show()
        
    elif pt==3:
        Darkscatter=ax.set_facecolor("lightsteelblue")
        plt.ylabel("Defense strength of pokemons")
        axs.scatter(Namei,Defensei,color="navy")
        plt.title("Name Vs defense strength")
        plt.show()

    elif pt==4:
        Darkscatter=ax.set_facecolor("lightgoldenrodyellow")
        plt.ylabel("ALL abilities of pokemons")
        axs.scatter(Namei,HPi,color="r",label="Name Vs HP")
        axs.scatter(Namei,Attacki,color="g",label="Name Vs Attack")
        axs.scatter(Namei,Defensei,color="m",label="Name Vs Defense")
        plt.title("complete analysis of pokemons")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")    
 

def Dragonbar():
    Dragon=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Dragon["Name"]
    HPi=Dragon["HP"]
    Attacki=Dragon["Attack"]
    Defensei=Dragon["Defense"]
    plt.xlabel("Name of pokemon")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one stackbar chart")
    print("press 5 to merge all the data in one multibar chart")
    
    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        dragonbar=ax.set_facecolor("navajowhite")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.bar(Namei,HPi)
        plt.xticks(rotation="vertical")
        plt.show()

    elif pt==2:
        dragonbar=ax.set_facecolor("bisque")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.bar(Namei,Attacki,color="r")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==3:
        dragonbar=ax.set_facecolor("lightpink")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.bar(Namei,Defensei,color="m")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==4:
        dragonbar=ax.set_facecolor("peachpuff")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs all abilities")
        plt.bar(Namei,HPi,width=0.2,label="Name Vs HP")
        plt.bar(Namei,Attacki,width=0.2,label="Name Vs Attack strength")
        plt.bar(Namei,Defensei,width=0.2,label="Name Vs defense strength")
        plt.xticks(rotation="vertical")
        plt.legend()
        plt.show()

    elif pt==5:
        dragonbar=ax.set_facecolor("peachpuff")
        VD=np.arange(len(Namei))
        plt.bar(VD,HPi,width=0.33,label="Name Vs HP")
        plt.bar(VD+0.33,Attacki,width=0.33,label="Name Vs Attack strength")
        plt.bar(VD+0.66,Defensei,width=0.33,label="Name Vs defense strength")
        plt.xticks(VD,Namei,rotation="vertical")
        plt.title("Name Vs all abilities")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")  


def Dragonhistogram():
    Dragon=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Totali=Dragon["Total"]
    Dragonhisto=ax.set_facecolor("mistyrose")
    plt.hist(Totali,bins=[300,400,500,600],color="m")
    plt.ylabel("Total Number of different DRAGON pokemons")
    plt.title("Range wise total number of Dragon pokemons")
    plt.xticks(rotation="vertical")
    plt.show()


def Dragonline():
    Dragon=pd.read_csv("D:\python projects\schoolproject\Dragon.csv")
    Namei=Dragon["Name"]
    HPi=Dragon["HP"]
    Attacki=Dragon["Attack"]
    Defensei=Dragon["Defense"]
    plt.xlabel("Name of pokemon")
    plt.xticks(rotation="vertical")
    
    print("press 1 to print the data for POKEMON v/s HP")
    print("press 2 to print the data for POKEMON v/s ATTACK")
    print("press 3 to print the data for POKEMON v/s DEFENCE")
    print("press 4 to print the data for POKEMON v/s ALL ABILITIES")


    pt=int(input("Enter your choice="))

    if pt==1:
        Dragonline=ax.set_facecolor("paleturquoise")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.plot(Namei,HPi,color="k",marker='d',markersize=11,markeredgecolor='orchid',markerfacecolor="darkblue",linestyle="dashed",linewidth=2,label="NAME V/S HP")
        plt.show()

    elif pt==2:
        Dragonline=ax.set_facecolor("paleturquoise")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.plot(Namei,Attacki,color="k",marker='d',markersize=11,markeredgecolor='orchid',markerfacecolor="darkblue",linestyle="dashed",linewidth=2,label="NAME V/S ATTACK")
        plt.show()
        

    elif pt==3:
        Darkline=ax.set_facecolor("paleturquoise")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.plot(Namei,Defensei,color="k",marker='d',markersize=11,markeredgecolor='orchid',markerfacecolor="darkblue",linestyle="dashed",linewidth=2,label="NAME V/S DEFENSE")
        plt.show()

    elif pt==4:
        Dragonline=ax.set_facecolor("paleturquoise")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.plot(Namei,HPi,color="b",label="NAME V/S HP")
        plt.plot(Namei,Attacki,color="k",label="NAME V/S ATTACK")
        plt.plot(Namei,Defensei,color="g",label="NAME V/S DEFENSE")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")  


def Dragonpie():
    Dragon=pd.read_csv("D:\python projects\schoolproject\Dragon.csv")
    Namei=Dragon["Name"]
    HPi=Dragon["HP"]
    Attacki=Dragon["Attack"]
    Defensei=Dragon["Defense"]

    print("press 1 for the data for name of pokemon Vs HP of pokemons")
    print("press 2 for the data for name of pokemon Vs Attack strength of pokemons")
    print("press 3 for the data for name of pokemon Vs Defense strength of pokemons")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        plt.title("name vs HP")
        plt.pie(HPi,labels=Namei)
        #autopct attribute can be used to show the percentage of the data.
        plt.show()
        

    elif pt==2:
        plt.title("Name Vs Attack strength")
        plt.pie(Attacki,labels=Namei)
        plt.show()
        
    elif pt==3:
        plt.title("Name Vs defense strength")
        plt.pie(Defensei,labels=Namei)
        plt.show()
    
    else:
        print("enter vaid input")


def Dragonscatter():
    Dragon=pd.read_csv("D:\python projects\schoolproject\Dragon.csv")
    Namei=Dragon["Name"]
    HPi=Dragon["HP"]
    Attacki=Dragon["Attack"]
    Defensei=Dragon["Defense"]
    plt.xlabel("Name of pokemons")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one scatter chart")

    axs=plt.gca()
    
    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        Dragonscatter=ax.set_facecolor("paleturquoise")
        plt.ylabel("HP of pokemons")
        ax.scatter(Namei,HPi,color="r")
        plt.title("Name vs HP")
        plt.show()
        
    elif pt==2:
        Dragonscatter=ax.set_facecolor("paleturquoise")
        plt.ylabel("Attack strength of pokemons")
        ax.scatter(Namei,Attacki,color="b")
        plt.title("Name vs Attack strength")
        plt.show()
        
    elif pt==3:
        Dragonscatter=ax.set_facecolor("paleturquoise")
        plt.ylabel("Defense strength of pokemons")
        ax.scatter(Namei,Defensei,color="darkgreen")
        plt.title("Name Vs defense strength")
        plt.show()

    elif pt==4:
        Dragonscatter=ax.set_facecolor("paleturquoise")
        plt.ylabel("All abilities of pokemons")
        ax.scatter(Namei,HPi,color="r",label="Name Vs HP")
        ax.scatter(Namei,Attacki,color="b",label="Name Vs Attack")
        ax.scatter(Namei,Defensei,color="darkgreen",label="Name Vs Defense")
        plt.title("complete analysis of pokemons")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")
 

def Electricbar():
    Electric=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Electric["Name"]
    HPi=Electric["HP"]
    Attacki=Electric["Attack"]
    Defensei=Electric["Defense"]
    plt.xlabel("Name of pokemon")
    ax=plt.axes()

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one stackbar chart")
    print("press 5 to merge all the data in one multibar chart")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        electricbar=ax.set_facecolor("navajowhite")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.bar(Namei,HPi)
        plt.xticks(rotation="vertical")
        plt.show()

    elif pt==2:
        electricbar=ax.set_facecolor("bisque")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.bar(Namei,Attacki,color="r")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==3:
        electricbar=ax.set_facecolor("lightpink")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.bar(Namei,Defensei,color="m")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==4:
        electricbar=ax.set_facecolor("peachpuff")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.bar(Namei,HPi,width=0.2,label="Name Vs HP")
        plt.bar(Namei,Attacki,width=0.2,label="Name Vs Attack strength")
        plt.bar(Namei,Defensei,width=0.2,label="Name Vs defense strength")
        plt.xticks(rotation="vertical")
        plt.legend()
        plt.show()

    elif pt==5:
        electricbar=ax.set_facecolor("peachpuff")
        VD=np.arange(len(Namei))
        plt.bar(VD,HPi,width=0.33,label="Name Vs HP")
        plt.bar(VD+0.33,Attacki,width=0.33,label="Name Vs Attack strength")
        plt.bar(VD+0.66,Defensei,width=0.33,label="Name Vs defense strength")
        plt.xticks(VD,Namei,rotation="vertical")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")       
        

def Electrichistogram():
    Electric=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Totali=Electric["Total"]
    Electrichisto=ax.set_facecolor("cornsilk")
    plt.hist(Totali,bins=[300,400,500,600],color="g")
    plt.ylabel("Total Number of different ELECTRIC pokemons")
    plt.title("Range wise total number of electric pokemons")
    plt.xticks(rotation="vertical")
    plt.show()


def electricline():
    electric=pd.read_csv("D:\python projects\schoolproject\Electric.csv")
    Namei=electric["Name"]
    HPi=electric["HP"]
    Attacki=electric["Attack"]
    Defensei=electric["Defense"]
    plt.xlabel("Name of pokemon")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one line chart")


    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        electricline=ax.set_facecolor("khaki")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.plot(Namei,HPi,"k",marker="s",markersize=8,markerfacecolor="peru",markeredgecolor="black",linestyle="dashdot",linewidth=2)
        plt.show()

    elif pt==2:
        electricline=ax.set_facecolor("khaki")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.plot(Namei,Attacki,"k",marker="s",markersize=8,markerfacecolor="peru",markeredgecolor="black",linestyle="dashdot",linewidth=2)
        plt.show()
        
    elif pt==3:
        electricline=ax.set_facecolor("khaki")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.plot(Namei,Defensei,"k",marker="s",markersize=8,markerfacecolor="peru",markeredgecolor="black",linestyle="dashdot",linewidth=2)
        plt.show()
        
    elif pt==4:
        electricline=ax.set_facecolor("khaki")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.plot(Namei,HPi,label="Name Vs HP")
        plt.plot(Namei,Attacki,label="Name Vs Attack strength")
        plt.plot(Namei,Defensei,label="Name Vs defense strength")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")
        


def Electricpie():
    Electric=pd.read_csv("D:\python projects\schoolproject\Electric.csv")
    Namei=Electric["Name"]
    HPi=Electric["HP"]
    Attacki=Electric["Attack"]
    Defensei=Electric["Defense"]

    print("press 1 for the data for name of pokemon Vs HP of pokemons")
    print("press 2 for the data for name of pokemon Vs Attack strength of pokemons")
    print("press 3 for the data for name of pokemon Vs Defense strength of pokemons")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        plt.title("name vs HP")
        plt.pie(HPi,labels=Namei)
        #autopct attribute can be used to show the percentage of the data.
        plt.show()
        

    elif pt==2:
        plt.title("Name Vs Attack strength")
        plt.pie(Attacki,labels=Namei)
        plt.show()
        
    elif pt==3:
        plt.title("Name Vs defense strength")
        plt.pie(Defensei,labels=Namei)
        plt.show()
    
    else:
        print("enter vaid input")

def Electricscatter():
    Electric=pd.read_csv("D:\python projects\schoolproject\Electric.csv")
    Namei=Electric["Name"]
    HPi=Electric["HP"]
    Attacki=Electric["Attack"]
    Defensei=Electric["Defense"]
    plt.xlabel("Name of pokemons")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one scatter chart")

    axs=plt.gca()
    
    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        electricscatter=ax.set_facecolor("papayawhip")
        axs.scatter(Namei,HPi,color="chocolate")
        plt.title("Name vs HP")
        plt.ylabel("HP of pokemons")
        plt.show()
        
    elif pt==2:
        electricscatter=ax.set_facecolor("papayawhip")
        axs.scatter(Namei,Attacki,color="limegreen")
        plt.title("Name vs Attack strength")
        plt.ylabel("attack strength of pokemons")
        plt.show()
        
    elif pt==3:
        electricscatter=ax.set_facecolor("papayawhip")
        axs.scatter(Namei,Defensei,color="cornflowerblue")
        plt.title("Name Vs defense strength")
        plt.ylabel("defense strength of pokemons")
        plt.show()

    elif pt==4:
        electricscatter=ax.set_facecolor("papayawhip")
        axs.scatter(Namei,HPi,color="chocolate",label="Name Vs HP")
        axs.scatter(Namei,Attacki,color="limegreen",label="Name Vs Attack")
        axs.scatter(Namei,Defensei,color="cornflowerblue",label="Name Vs Defense")
        plt.title("complete analysis of pokemons")
        plt.ylabel("all abilities of pokemons")
        plt.legend()
        plt.show()


    else:
        print("enter valid input")     


def Fairybar():
    Fairy=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Fairy["Name"]
    HPi=Fairy["HP"]
    Attacki=Fairy["Attack"]
    Defensei=Fairy["Defense"]
    plt.xlabel("Name of pokemon")
    ax=plt.axes()

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one stackbar chart")
    print("press 5 to merge all the data in one multibar chart")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        fairybar=ax.set_facecolor("navajowhite")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.barh(Namei,HPi)
        plt.xticks(rotation="vertical")
        plt.show()

    elif pt==2:
        fairybar=ax.set_facecolor("bisque")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.barh(Namei,Attacki,color="r")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==3:
        fairybar=ax.set_facecolor("lightpink")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.barh(Namei,Defensei,color="m")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==4:
        fairybar=ax.set_facecolor("peachpuff")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.bar(Namei,HPi,width=0.2,label="Name Vs HP")
        plt.bar(Namei,Attacki,width=0.2,label="Name Vs Attack strength")
        plt.bar(Namei,Defensei,width=0.2,label="Name Vs defense strength")
        plt.xticks(rotation="vertical")
        plt.legend()
        plt.show()

    elif pt==5:
        fairybar=ax.set_facecolor("peachpuff")
        VD=np.arange(len(Namei))
        plt.bar(VD,HPi,width=0.33,label="Name Vs HP")
        plt.bar(VD+0.33,Attacki,width=0.33,label="Name Vs Attack strength")
        plt.bar(VD+0.66,Defensei,width=0.33,label="Name Vs defense strength")
        plt.xticks(VD,Namei,rotation="vertical")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")    
 

def Fairyhistogram():
    Fairy=pd.read_csv("D:\python projects\schoolproject\Fairy.csv")
    Totali=Fairy["Total"]
    Fairyhisto=ax.set_facecolor("antiquewhite")
    plt.hist(Totali,bins=[300,400,500,600],color="c")
    plt.ylabel("Total Number of different FAIRY pokemons")
    plt.title("Range wise total number of Fairy pokemons")
    plt.xticks(rotation="vertical")
    plt.show()


def Fairyline():
    Fairy=pd.read_csv("D:\python projects\schoolproject\Fairy.csv")
    Namei=Fairy["Name"]
    HPi=Fairy["HP"]
    Attacki=Fairy["Attack"]
    Defensei=Fairy["Defense"]
    plt.xlabel("Name of pokemon")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one line chart")


    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        Fairyline=ax.set_facecolor("peachpuff")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.plot(Namei,HPi,"r",marker="D",markersize=9,markerfacecolor="maroon",markeredgecolor="royalblue",linestyle="solid",linewidth=2)
        plt.show()

    elif pt==2:
        Fairyline=ax.set_facecolor("peachpuff")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.plot(Namei,Attacki,"r",marker="D",markersize=9,markerfacecolor="maroon",markeredgecolor="royalblue",linestyle="solid",linewidth=2)
        plt.show()
        
    elif pt==3:
        Fairyline=ax.set_facecolor("peachpuff")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.plot(Namei,Defensei,"r",marker="D",markersize=9,markerfacecolor="maroon",markeredgecolor="royalblue",linestyle="solid",linewidth=2)
        plt.show()
        
    elif pt==4:
        Fairyline=ax.set_facecolor("cornsilk")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.plot(Namei,HPi,label="Name Vs HP")
        plt.plot(Namei,Attacki,label="Name Vs Attack strength")
        plt.plot(Namei,Defensei,label="Name Vs defense strength")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")

def Fairypie():
    Fairy=pd.read_csv("D:\python projects\schoolproject\Fairy.csv")
    Namei=Fairy["Name"]
    HPi=Fairy["HP"]
    Attacki=Fairy["Attack"]
    Defensei=Fairy["Defense"]

    print("press 1 for the data for name of pokemon Vs HP of pokemons")
    print("press 2 for the data for name of pokemon Vs Attack strength of pokemons")
    print("press 3 for the data for name of pokemon Vs Defense strength of pokemons")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        plt.title("name vs HP")
        plt.pie(HPi,labels=Namei)
        #autopct attribute can be used to show the percentage of the data.
        plt.show()
        

    elif pt==2:
        plt.title("Name Vs Attack strength")
        plt.pie(Attacki,labels=Namei)
        plt.show()
        
    elif pt==3:
        plt.title("Name Vs defense strength")
        plt.pie(Defensei,labels=Namei)
        plt.show()
    
    else:
        print("enter vaid input")


def Fairyscatter():
    Fairy=pd.read_csv("D:\python projects\schoolproject\Fairy.csv")
    Namei=Fairy["Name"]
    HPi=Fairy["HP"]
    Attacki=Fairy["Attack"]
    Defensei=Fairy["Defense"]
    plt.xlabel("Name of pokemons")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one scatter chart")

    axs=plt.gca()
    
    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        Fairyscatter=ax.set_facecolor("bisque")
        axs.scatter(Namei,HPi,color="r")
        plt.ylabel("Hp of pokemons")
        plt.title("Name vs HP")
        plt.show()
        
    elif pt==2:
        Fairyscatter=ax.set_facecolor("bisque")
        axs.scatter(Namei,Attacki,color="m")
        plt.ylabel("attack strength of pokemons")
        plt.title("Name vs Attack strength")
        plt.show()
        
    elif pt==3:
        Fairyscatter=ax.set_facecolor("bisque")
        axs.scatter(Namei,Defensei,color="teal")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.show()

    elif pt==4:
        Fairyscatter=ax.set_facecolor("bisque")
        axs.scatter(Namei,HPi,color="r",label="Name Vs HP")
        axs.scatter(Namei,Attacki,color="m",label="Name Vs Attack")
        axs.scatter(Namei,Defensei,color="teal",label="Name Vs Defense")
        plt.ylabel("all abilities")
        plt.title("complete analysis of pokemons")
        plt.legend()
        plt.show()
    else:
        print("enter valid input")  
 

def Fightingbar():
    Fighting=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Namei=Fighting["Name"]
    HPi=Fighting["HP"]
    Attacki=Fighting["Attack"]
    Defensei=Fighting["Defense"]
    plt.xlabel("Name of pokemon")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one stackbar chart")
    print("press 5 to merge all the data in one multibar chart")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        fightingbar=ax.set_facecolor("navajowhite")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.bar(Namei,HPi)
        plt.xticks(rotation="vertical")
        plt.show()

    elif pt==2:
        fightingbar=ax.set_facecolor("bisque")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.bar(Namei,Attacki,color="r")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==3:
        fightingbar=ax.set_facecolor("lightpink")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.bar(Namei,Defensei,color="m")
        plt.xticks(rotation="vertical")
        plt.show()
        
    elif pt==4:
        fightingbar=ax.set_facecolor("peachpuff")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.bar(Namei,HPi,width=0.2,label="Name Vs HP")
        plt.bar(Namei,Attacki,width=0.2,label="Name Vs Attack strength")
        plt.bar(Namei,Defensei,width=0.2,label="Name Vs defense strength")
        plt.xticks(rotation="vertical")
        plt.legend()
        plt.show()

    elif pt==5:
        fightingbar=ax.set_facecolor("peachpuff")
        VD=np.arange(len(Namei))
        plt.bar(VD,HPi,width=0.33,label="Name Vs HP")
        plt.bar(VD+0.33,Attacki,width=0.33,label="Name Vs Attack strength")
        plt.bar(VD+0.66,Defensei,width=0.33,label="Name Vs defense strength")
        plt.xticks(VD,Namei,rotation="vertical")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")


def Fightinghistogram():
    Fighting=pd.read_csv("D:\python projects\schoolproject\Bug.csv")
    Totali=Fighting["Total"]
    Fightinghisto=ax.set_facecolor("lightblue")
    plt.hist(Totali,bins=[300,400,500,600],color="r")
    plt.ylabel("Total Number of different Fighting pokemons")
    plt.title("Range wise total number of fighting pokemons")
    plt.xticks(rotation="vertical")
    plt.show()


def Fightingline():
    Fighting=pd.read_csv("D:\python projects\schoolproject\Fighting.csv")
    Namei=Fighting["Name"]
    HPi=Fighting["HP"]
    Attacki=Fighting["Attack"]
    Defensei=Fighting["Defense"]
    plt.xlabel("Name of pokemon")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one line chart")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        Fightingline=ax.set_facecolor("blanchedalmond")
        plt.ylabel("HP of pokemons")
        plt.title("Name Vs HP")
        plt.plot(Namei,HPi,"m",marker="h",markersize=11,markerfacecolor="blue",markeredgecolor="darkgreen",linestyle="solid",linewidth=3)
        plt.show()

    elif pt==2:
        Fightingline=ax.set_facecolor("blanchedalmond")
        plt.ylabel("attaking strength of pokemons")
        plt.title("Name Vs Attack strength")
        plt.plot(Namei,Attacki,"m",marker="h",markersize=11,markerfacecolor="blue",markeredgecolor="darkgreen",linestyle="solid",linewidth=3)
        plt.show()
        
    elif pt==3:
        Fightingline=ax.set_facecolor("blanchedalmond")
        plt.ylabel("defense strength of pokemons")
        plt.title("Name Vs defense strength")
        plt.plot(Namei,Defensei,"m",marker="h",markersize=11,markerfacecolor="blue",markeredgecolor="darkgreen",linestyle="solid",linewidth=3)
        plt.show()
        
    elif pt==4:
        Fightingline=ax.set_facecolor("lemonchiffon")
        plt.ylabel("HP,Attack and defense strength")
        plt.title("Name Vs abilities")
        plt.plot(Namei,HPi,label="Name Vs HP")
        plt.plot(Namei,Attacki,label="Name Vs Attack strength")
        plt.plot(Namei,Defensei,label="Name Vs defense strength")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")

def Fightingpie():
    Fighting=pd.read_csv("D:\python projects\schoolproject\Fighting.csv")
    Namei=Fighting["Name"]
    HPi=Fighting["HP"]
    Attacki=Fighting["Attack"]
    Defensei=Fighting["Defense"]

    print("press 1 for the data for name of pokemon Vs HP of pokemons")
    print("press 2 for the data for name of pokemon Vs Attack strength of pokemons")
    print("press 3 for the data for name of pokemon Vs Defense strength of pokemons")

    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        plt.title("name vs HP")
        plt.pie(HPi,labels=Namei)
        #autopct attribute can be used to show the percentage of the data.
        plt.show()
        
    elif pt==2:
        plt.title("Name Vs Attack strength")
        plt.pie(Attacki,labels=Namei)
        plt.show()
        
    elif pt==3:
        plt.title("Name Vs defense strength")
        plt.pie(Defensei,labels=Namei)
        plt.show()
    
    else:
        print("enter vaid input")

def Fightingscatter():
    Fighting=pd.read_csv("D:\python projects\schoolproject\Fighting.csv")
    Namei=Fighting["Name"]
    HPi=Fighting["HP"]
    Attacki=Fighting["Attack"]
    Defensei=Fighting["Defense"]
    plt.xlabel("Name of pokemons")
    plt.xticks(rotation="vertical")

    print("press 1 for the data for name of pokemon Vs HP")
    print("press 2 for the data for name of pokemon Vs Attack")
    print("press 3 for the data for name of pokemon Vs Defense")
    print("press 4 to merge all the data in one scatter chart")

    axs=plt.gca()
    
    pt=int(input("enter what type of graph u want to see:"))

    if pt==1:
        Fightingscatter=ax.set_facecolor("mistyrose")
        axs.scatter(Namei,HPi,color="blue")
        plt.ylabel("HP of Pokemons")
        plt.title("Name vs HP")
        plt.show()
        
    elif pt==2:
        Fightingscatter=ax.set_facecolor("mistyrose")
        axs.scatter(Namei,Attacki,color="crimson")
        plt.title("Name vs Attack strength")
        plt.ylabel("Attack strength of Pokemons")
        plt.show()
        
    elif pt==3:
        Fightingscatter=ax.set_facecolor("mistyrose")
        axs.scatter(Namei,Defensei,color="dodgerblue")
        plt.ylabel("Defense strength of Pokemons")
        plt.title("Name Vs defense strength")
        plt.show()

    elif pt==4:
        Fightingscatter=ax.set_facecolor("mistyrose")
        axs.scatter(Namei,HPi,color="blue",label="Name Vs HP")
        axs.scatter(Namei,Attacki,color="crimson",label="Name Vs Attack")
        axs.scatter(Namei,Defensei,color="dodgerblue",label="Name Vs Defense")
        plt.ylabel("all abilities of pokemons")
        plt.title("complete analysis of pokemons")
        plt.legend()
        plt.show()

    else:
        print("enter valid input")



