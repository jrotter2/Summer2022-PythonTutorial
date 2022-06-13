# Summer 2022 - Python Tutorial
Simple Python/ROOT Tutorial for CMS@Rice Summer 2022

## Logging into a Cluster
### Lxplus
Lxplus is the CERN computing cluster based in Geneva. Using your cern credentials to login,
```
ssh <username>@lxplus.cern.ch>
(Prompted to put password)
```
### cmslpc
cmslpc is the FNAL computing cluster based in Chicago. Login requires downloading a Kerberos configuration file and modifying your .ssh. Directions can be found [here](https://uscms.org/uscms_at_work/computing/getstarted/uaf.shtml)
Using your FNAL credentials you then do,
```
kinit <username>@FNAL.gov
(Prompted to put password)

ssh -Y <username>@cmslpc-sl7.fnal.gov

```
