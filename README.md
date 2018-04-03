<p align="center">
  <a href="" rel="noopener">
 <img width=300px src="logo.png" alt="HelpOff-logo"></a>
</p>

<h3 align="center">providing help via offline system</h3>

<div align="center">

[![Website cv.lbesson.qc.to](https://img.shields.io/website-up-down-green-red/http/cv.lbesson.qc.to.svg)](https://github.com/inishchith/HelpOff/tree/master)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

</div>

------------------------------------------

>Any information can be easily found by using `Google`, but `32%` of our population don't have  `Smartphone` and also there are many people having smartphone but no internet access round the clock due to which people suffer a lot for finding basic needs especially when travelling to a particularplace.  We've built a `SMS based offline system` where the user can get the required information in few basic steps by simple sending a message.


<div align="center">
&#10077; Internet is great but survival without Internet is the key. &#10078;  -  <a href ="https://github.com/shivam1708"> cheetAh </a>
</div>


------------------------------------------
### Features

<div align = "center">
<img src="./assets/helpoff1.gif" width=230px>
<img src="./assets/helpoff2.gif" width=230px>
<img src="./assets/helpoff3.gif" width=230px>

</div>

#### Find Nearby :
- `Hospitals`
- `Medical Stores`
- `Gas Stations`
- `Police Stations`
- `Railway Stations`
- `Taxi Stands`

user just provides the pin code followed by type of service:

```
400708 
nearby gas station
```
returns
```
Bharat Petroleum Airoli Service Centre
BPCL Petrol Pump, Plot No. 33, 
Sector 5, Airoli, Sector 5, 
Airoli, Navi Mumbai, Maharashtra 400708
```
#### Route 
In case a user wants to go to a particular location the system will provide information with proper guidance with various possible modes selected by the user(eg walking, train, etc)
Just Provide short address of starting address and destination address followed by mode of transport and you'll be shown the best way
```
show routes from 
sec10 Airoli
Somaiya VidyaVihar
driving
```
returns
```
Start:Sector 10 Rd, Sector 10, 
Airoli, Navi Mumbai, 
Maharashtra 400708
End:Somaiya Vidyavihar, 
Group of Somaiya Institutions, 
Vidyanagar, Vidya Vihar East, 
Vidyavihar, Mumbai, 
Maharashtra 400077
estimated time:22 mins
Get on Eastern Express Hwy/Mumbai - Agra National Hwy in Mulund East, Mumbai from Mulund - Airoli Rd
Follow Eastern Express Hwy/Mumbai - Agra National Hwy to Kamraj Nagar Rd in Nalanda Nagar
Take Olmstead Ave/Vidayabhavan Marg, 90 Feet Rd/Barrister Nath Pai Rd, Ghatkopar - Mahul Rd and Rd Number 7 to Sarvoday Buddh Vihar Marg in ONGC Colony
```
#### Complete Address
Many Times in daily life what happens is we know only the name of establishment and city but not any other details.If the establishment is not considerably popular it becomes an uphill task to find the real location in such a case a single line saying complete address followed by how muchever address you are aware of will return the complete address of the best possible match so you can reach you location easily

```
detailed address
sheffield apartments
dahisar
```
returns
```
Sheffield CHS 
C.S.Road, Anand Nagar 
Dahisar East, Mumbai, 
Maharashtra 400068
```
------------------------------------------
### Add-Ons

- [ ] Offline booking of cabs ( OLA / Uber ) 
- [ ] Provide generalized search options
- [ ] Book emergency service lines
- [ ] Create Distress messages
- [ ] Add More

------------------------------------------

### Problems-Overcome

- [ ] Bringing help offline.
- [ ] Natural Language Processing ability by courtesy of diagflow.
- [ ] Providing facility for feature phone user.
- [ ] Providing facility at bare minimum cost of sending SMS. 

------------------------------------------

### Problems Yet to Overcome

- [ ] Better Way to input the location.
- [ ] Provide better and smoother interface.
- [ ] Build a better UI based offline app like M-Indicator although sacrificing feature phones.

------------------------------------------

### Installation

* Install dependencies
```sh
        $ pip3 install -r requirements.txt
```

* Edit [config.py](https://github.com/inishchith/HelpOff/blob/master/App/config.py)

------------------------------------------
### Contributing

 We're are open to `enhancements` & `bug-fixes` :smile: Also do have a look [here](./CONTRIBUTING.md)

### Note

- This project was done under `12 hours`

------------------------------------------
### Contributors

- [@nurdtechie98](https://github.com/nurdtechie98)
- [@shivam98](https://github.com/shivam1708)
- [@inishchith](https://github.com/inishchith)

------------------------------------------
### Recognition

This repository / project was a part of **[@Hack-n-code Hackathon]('') 2018** where it got recognized as the **best ideation**.
