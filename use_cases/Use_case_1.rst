Use case № 1
------------

This notebook produces Effective Area (Aeff), Point Spread Function
(PSF), Energy Dispersion (Edisp) files in .fits format from original
KM3NeT simulation dst.root file

.. code:: ipython3

    from km3irf import build_irf
    from astropy.io import fits

Define a path to your local ``dst.root`` file:

.. code:: ipython3

    # data_path = "/run/media/msmirnov/iron_2tb/IRF_data_create/mcv5.1.km3_numuCC.ALL.dst.bdt.root"
    # data_path = "/home/msmirnov/working_space/IRF_data_create/mcv5.1.km3_numuCC.ALL.dst.bdt.root"
    # data_path = "/home/msmirnov/working_space/some_data/files_cta_km3net/mcv5.1.km3_numuCC.ALL.dst.bdt.root"
    data_path = "/run/media/msmirnov/DATA2/data_files/IRF_data_create/mcv5.1.km3_numuCC.ALL.dst.bdt.root"

Effective Area
~~~~~~~~~~~~~~

Create BuildAeff object:

.. code:: ipython3

    test_irf = build_irf.DataContainer(data_path)

How many events in the file:

.. code:: ipython3

    test_irf.df.shape[0]




.. parsed-literal::

    802872



.. code:: ipython3

    test_irf.df.head(4)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>E</th>
          <th>dir_x</th>
          <th>dir_y</th>
          <th>dir_z</th>
          <th>E_mc</th>
          <th>dir_x_mc</th>
          <th>dir_y_mc</th>
          <th>dir_z_mc</th>
          <th>weight_w2</th>
          <th>bdt0</th>
          <th>bdt1</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>349.621209</td>
          <td>-0.670299</td>
          <td>0.270036</td>
          <td>0.691216</td>
          <td>268.990</td>
          <td>-0.670996</td>
          <td>0.286741</td>
          <td>0.683772</td>
          <td>4.510000e+11</td>
          <td>12.0</td>
          <td>-2.000000</td>
        </tr>
        <tr>
          <th>1</th>
          <td>20.423436</td>
          <td>0.327411</td>
          <td>0.078130</td>
          <td>-0.941646</td>
          <td>178.710</td>
          <td>0.327387</td>
          <td>0.079789</td>
          <td>-0.941515</td>
          <td>1.182000e+11</td>
          <td>1.0</td>
          <td>-2.000000</td>
        </tr>
        <tr>
          <th>2</th>
          <td>184.966630</td>
          <td>0.794867</td>
          <td>0.354793</td>
          <td>-0.492248</td>
          <td>214.610</td>
          <td>0.799260</td>
          <td>0.353143</td>
          <td>-0.486285</td>
          <td>1.960000e+11</td>
          <td>1.0</td>
          <td>-2.000000</td>
        </tr>
        <tr>
          <th>3</th>
          <td>52.327015</td>
          <td>0.455668</td>
          <td>-0.632999</td>
          <td>0.625843</td>
          <td>291.347</td>
          <td>0.432161</td>
          <td>-0.625802</td>
          <td>0.649314</td>
          <td>5.622000e+11</td>
          <td>11.0</td>
          <td>0.998906</td>
        </tr>
      </tbody>
    </table>
    </div>



Apply user defined cuts:

.. code:: ipython3

    test_irf.apply_cuts()
    test_irf.df.shape[0]




.. parsed-literal::

    331325



Apply re-weighting procedure

.. code:: ipython3

    weighted_dict = test_irf.weight_calc(tag="nu", df_pass=test_irf.df)
    weighted_dict.values()




.. parsed-literal::

    dict_values([array([8.43265542e+00, 7.72364843e+00, 7.77098987e+00, ...,
           1.99530627e-05, 2.18194734e-05, 1.78086831e-05])])



Build .fits for effective area, it needs to specify the input pandas
data frame.

.. code:: ipython3

    test_irf.build_aeff(df_pass=test_irf.df)


.. parsed-literal::

    file aeff.fits is written successfully!
    

Check the output file with ``gammapy``

.. code:: ipython3

    # install gammapy if it needs
    #!pip install gammapy
    from gammapy.irf import EffectiveAreaTable2D

.. code:: ipython3

    # Read effective area IRFs
    aeff = EffectiveAreaTable2D.read("aeff.fits", hdu="EFFECTIVE AREA")
    print(aeff)


.. parsed-literal::

    EffectiveAreaTable2D
    --------------------
    
      axes  : ['energy_true', 'offset']
      shape : (48, 12)
      ndim  : 2
      unit  : m2
      dtype : >f8
    
    

.. code:: ipython3

    aeff.peek()



.. image:: Use_case_1_files%5CUse_case_1_19_0.png


Point Spread Function
~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    test_irf.build_psf(df_pass=test_irf.df)


.. parsed-literal::

    file psf.fits is written successfully!
    

.. parsed-literal::

    /home/msmirnov/working_space/km3irf/src/km3irf/build_irf.py:204: RuntimeWarning: invalid value encountered in divide
      psf = np.nan_to_num(psf / norm_psf_sm)
    

Check the output file ``psf.fits`` with ``gammapy``:

.. code:: ipython3

    from gammapy.irf import PSF3D

.. code:: ipython3

    psf = PSF3D.read("psf.fits", hdu="PSF_2D_TABLE")
    print(psf)


.. parsed-literal::

    PSF3D
    -----
    
      axes  : ['energy_true', 'offset', 'rad']
      shape : (24, 6, 111)
      ndim  : 3
      unit  : 1 / sr
      dtype : >f8
    
    

.. code:: ipython3

    psf.peek()



.. image:: Use_case_1_files%5CUse_case_1_25_0.png


Energy dispertion
~~~~~~~~~~~~~~~~~

.. code:: ipython3

    test_irf.build_edisp(df_pass=test_irf.df, norm=True, smooth=False, smooth_norm=False)


.. parsed-literal::

    file edisp.fits is written successfully!
    

.. parsed-literal::

    /home/msmirnov/working_space/km3irf/src/km3irf/build_irf.py:256: RuntimeWarning: invalid value encountered in divide
      edisp = np.nan_to_num(edisp / m_normed.sum(axis=1, keepdims=True))
    

Check the output file ``edisp.fits`` with ``gammapy``:

.. code:: ipython3

    from gammapy.irf import EnergyDispersion2D

.. code:: ipython3

    edisp = EnergyDispersion2D.read("edisp.fits", hdu="EDISP_2D")
    print(edisp)


.. parsed-literal::

    EnergyDispersion2D
    ------------------
    
      axes  : ['energy_true', 'migra', 'offset']
      shape : (24, 56, 6)
      ndim  : 3
      unit  : 
      dtype : >f8
    
    

.. code:: ipython3

    edisp.peek()



.. image:: Use_case_1_files%5CUse_case_1_31_0.png


Write all created fits files to the one combined IRF file.

.. code:: ipython3

    from km3irf.utils import merge_fits

background is takken from ``km3irf`` data folder

.. code:: ipython3

    merge_fits(
        aeff_fits="aeff.fits",
        psf_fits="psf.fits",
        edisp_fits="edisp.fits",
        output_path=".",
        output_file="combined_IRF.fits",
    )


.. parsed-literal::

    combined IRF file combined_IRF.fits is written successfully!
    
