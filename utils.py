"""Common utility functions and radar relationships"""

__author__ = 'Cyril Grima'

#from numpy import arcsin, cos, pi, sin, sqrt
import numpy as np
import scipy.constants as ct


#-------------------
# Common conversions
#-------------------


def deg2rad(x):
    """Degree to Radian"""
    return x*np.pi/180


def rad2deg(x):
    """Radian to Degree"""
    return x*180/np.pi


def wf2wl(x):
    """Wavelength to frequency"""
    return ct.c/x


def wl2wf(x):
    """Wavelength to frequency"""
    return ct.c/x


def wl2wk(x):
    """Wavelength to wave number"""
    return 2*np.pi/x


def wf2wk(x):
    """Frequency to wave number"""
    return 2*np.pi/wf2wl(x)


def wk2vec(wk, th):
    """Scalar to Vectorial wave number"""
    return {'x':wk*np.sin(th), 'z':wk*np.cos(th)}


#---------------------
# Fresnel/Snell's Laws
#---------------------


def theta_i2t(x, n1, n2):
    """Incident to transmission angle conversion"""
    return np.arcsin(np.sin(x)*n1/n2)


def theta_t2i(x, n1, n2):
    """Incident to transmission angle conversion"""
    return np.arcsin(np.sin(x)*n2/n1)


def epmu2n(ep, mu):
    """Relative electric perm. and magnetic perm. to optical index"""
    return np.sqrt(ep*mu)


def R_v(ep1, ep2, mu1, mu2, xi):
    """Vertical (parallel) reflection coeff, funct. of incident angle"""
    n1 = epmu2n(ep1, mu1)
    n2 = epmu2n(ep2, mu2)
    xt = theta_i2t(xi, n1, n2)
    z1, z2 = np.sqrt(mu1/ep1), np.sqrt(mu2/ep2)
    return (z2*np.cos(xt) - z1*np.cos(xi)) / (z2*np.cos(xt) + z1*np.cos(xi))


def T_v(ep1, ep2, mu1, mu2, xi):
    """Vertical (parallel) transmission coeff, funct. of incident angle"""
    n1 = epmu2n(ep1, mu1)
    n2 = epmu2n(ep2, mu2)
    xt = theta_i2t(xi, n1, n2)
    z1, z2 = np.sqrt(mu1/ep1), np.sqrt(mu2/ep2)
    return 2*z2*np.cos(xi) / (z2*np.cos(xt) + z1*np.cos(xi))


def R_h(ep1, ep2, mu1, mu2, xi):
    """Horizontal (perpandicular) reflection coeff, funct. of incident angle"""
    n1 = epmu2n(ep1, mu1)
    n2 = epmu2n(ep2, mu2)
    xt = theta_i2t(xi, n1, n2)
    z1, z2 = np.sqrt(mu1/ep1), np.sqrt(mu2/ep2)
    return (z2*np.cos(xi) - z1*np.cos(xt)) / (z2*np.cos(xi) + z1*np.cos(xt))


def T_h(ep1, ep2, mu1, mu2, xi):
    """Horizontal (perpandicular) transmission coeff, funct. of inc. angle"""
    n1 = epmu2n(ep1, mu1)
    n2 = epmu2n(ep2, mu2)
    xt = theta_i2t(xi, n1, n2)
    z1, z2 = np.sqrt(mu1/ep1), np.sqrt(mu2/ep2)
    return 2*z2*np.cos(xi) / (z2*np.cos(xi) + z1*np.cos(xt))


def R(ep1, ep2, mu1, mu2, xi):
    """Unpolarized Reflection coefficient"""
    return (R_v(ep1, ep2, mu1, mu2, xi) + R_h(ep1, ep2, mu1, mu2, xi))/2.


#---------------------
# Footprints
#---------------------


def footprint_rad_beam(h, bmw):
    """radius of the beam-limited footprint"""
    return np.abs(h)*bmw/2.

def footprint_rad_pulse(h, bw):
    """radius of the pulse-limited footprint"""
    return np.sqrt(np.abs(h)*ct.c/bw)

def footprint_rad_fresnel(h, wl):
    """radius of the Fresnel footprint"""
    return np.sqrt(np.abs(h)*wl/2)


#------
# Misc.
#------

def geo_loss(h):
    """Energy losses from geometric spreading"""
    return 1/(4*np.pi*h**2)
