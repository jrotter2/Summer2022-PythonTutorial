############## IMPORTS ##############

import ROOT
import math

############## FUNCTIONS ##############
# We want function that const*e^(-(x-mu)*(x-mu) / ((2*sigma)*(2*sigma))) + a + b*x + c*x*x DONE!

def gausppar(xs, params):
   """
      param[0] -> const
      param[1] -> mu
      param[2] -> sigma
      param[3] -> a
      param[4] -> b
      param[5] -> c
   """
   return params[0] * math.exp((xs[0] - params[1])*(xs[0] - params[1]) / ((2*params[2])*(2*params[2]))) + params[3] + params[4]*xs[0] + params[5]*xs[0]*xs[0];

############## MAIN SCRIPT CALL ##############

if __name__ == "__main__":

   # Defining variables
   const = 4
   mu = 7
   sigma = 1
   a = 15
   b = -1.2
   c = .03

   # Initialize Function (TF1)
   gausppar = ROOT.TF1('gausppar', gausppar, 20, -1, 21)
   gausppar.SetParameters(const, mu, sigma, a, b, c)
   # Initialize Histogram (TH1F)
   raw = ROOT.TH1F('raw', 'Raw Distribution', 50, -.5, 20.5) 
   raw.SetMarkerStyle(20) #DOT
   raw.SetMarkerSize(.3) #SMALL DOTS
   raw.SetLineColor(1) # Makes Black Line

   # Fill the histogram with 5000 random numbers from our function
   raw.FillRandom('gausppar', 5000)


   # Reset our function's parameters back to 1 (Or reasonable value)

   # Fitting the histogram with our function

   # Initalizing Canvas and Plotting
   #c = ROOT.TCanvas("overlay","canvas",400,400)
   #legend = ROOT.TLegend (0.65 ,0.6 ,0.85 ,0.75)
   #legend.SetTextSize(.02)

   # Draw the histogram with Error Bars



   # Initializing Annotations
   #latex = ROOT.TLatex() 
   #latex.SetNDC()
   #latex.SetTextSize(0.04)
   #latex.DrawLatex(0.12 ,0.85 , "CMS #font[52]{Preliminary Simulation}")
   #latex.SetTextSize(0.03)
   #latex.DrawLatex(0.12 ,0.82 , "#font[52]{#it{Tutorial}}")
   #legend.SetLineWidth (0)
   #legend.Draw("same")

   # Saving to PDF
   #c.Print("tutorial_plot.pdf")
