############## IMPORTS ##############

import ROOT
import math

############## FUNCTIONS ##############

def guasspar(x, pars):
   return pars[0]*math.exp(-(x[0]-pars[1])*(x[0]-pars[1]) / ((2*pars[2])*(2*pars[2]))) + pars[3] + pars[4]*x[0] + pars[5]*x[0]*x[0]


############## MAIN SCRIPT CALL ##############

if __name__ == "__main__":

   # Defining variables
   const = 4
   mu = 7
   sigma = 1
   a = 15
   b = -1.2
   c = .03

   # Initializing Function (TF1)
   guasppar = ROOT.TF1('guasppar', guasspar, 20, -1, 21)
   guasppar.SetParameters(const, mu, sigma, a, b, c)

   # Initializing Histogram (TH1F)
   raw = ROOT.TH1F('raw', 'Raw Distribution', 50, -0.5, 20.5)
   raw.SetMarkerStyle(20) # Sets marker to a dot
   raw.SetMarkerSize(.3) # Sets marker to be a small dot 
   raw.SetLineColor(1) # Sets line color to black

   raw.FillRandom('guasppar', 5000) # Fills the histogram with 5000 random numbers from our function


   # Reseting out function's parameters back to 1 (Or reasonable value)
   guasppar.SetParameter(0,50);
   guasppar.SetParameter(1,6);
   guasppar.SetParameter(2,1);
   guasppar.SetParameter(3,1);
   guasppar.SetParameter(4,1);
   guasppar.SetParameter(5,1);

   # Fitting the histogram with our function
   fit = raw.Fit(guasppar, "S");

   # Initalizing Canvas and Plotting
   c = ROOT.TCanvas("overlay","canvas",400,400)
   legend = ROOT.TLegend (0.65 ,0.6 ,0.85 ,0.75)
   legend.SetTextSize(.02)
   raw.Draw("PE") # PE option will draw Error Bars
   #raw.Draw("same")

   # Initializing Annotations
   latex = ROOT.TLatex() 
   latex.SetNDC()
   latex.SetTextSize(0.04)
   latex.DrawLatex(0.12 ,0.85 , "CMS #font[52]{Preliminary Simulation}")
   latex.SetTextSize(0.03)
   latex.DrawLatex(0.12 ,0.82 , "#font[52]{#it{Tutorial}}")
   legend.SetLineWidth (0)
   legend.Draw("same")

   # Saving to PDF
   c.Print("tutorial_plot.pdf")

