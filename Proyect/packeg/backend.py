

class references:
    def __init__(self,
                references,
                cliente,
                tipo_Vehiculo,
                num_Vehiculo,
                Status,
                scac,
                tod_Fecha,
                tod_Time,
                tnf_Fecha,
                tnf_Time,
                dxs_Fecha,
                dxs_Time,
                dly_Fecha,
                dly_Time,
                dly_Notes,
                afs_Fecha,
                afs_Time,
                dpu_Fecha,
                dpu_Time,
                exr_Fecha,
                exr_Time,
                exr_Notes,
                ecc_Fecha,
                ecc_Time,
                ilr_Fecha,
                ilr_Time,
                ilr_Tipo,
                ilr_Notes,
                clr_Fecha,
                clr_Time,
                st1_Fecha,
                st1_Time,
                st1_Notes,
                tsc_Time,
                tsc_Fecha,
                tsc_Notes
                ):
        self.references= references
        self.cliente=cliente
        self.tipo_Vehiculo=tipo_Vehiculo
        self.num_Vehiculo=num_Vehiculo
        self.Status=Status
        self.scac=scac
        self.tod_Fecha=tod_Fecha
        self.tod_Time=tod_Time
        self.tnf_Fecha=tnf_Fecha
        self.tnf_Time=tnf_Time
        self.dxs_Fecha=dxs_Fecha
        self.dxs_Time=dxs_Time
        self.dly_Fecha=dly_Fecha
        self.dly_Time=dly_Time
        self.dly_Notes=dly_Notes
        self.afs_Fecha=afs_Fecha
        self.afs_Time=afs_Time
        self.dpu_Fecha=dpu_Fecha
        self.dpu_Time=dpu_Time
        self.exr_Fecha=exr_Fecha
        self.exr_Time=exr_Time
        self.exr_Notes=exr_Notes
        self.ecc_Fecha=ecc_Fecha
        self.ecc_Time=ecc_Time
        self.ilr_Fecha=ilr_Fecha
        self.ilr_Time=ilr_Time
        self.ilr_Tipo=ilr_Tipo
        self.ilr_Notes=ilr_Notes
        self.clr_Fecha=clr_Fecha
        self.clr_Time=clr_Time
        self.st1_Fecha=st1_Fecha
        self.st1_Time=st1_Time
        self.st1_Notes=st1_Notes
        self.tsc_Time=tsc_Time
        self.tsc_Fecha=tsc_Fecha
        self.tsc_Notes=tsc_Notes

    @property 
    def references(self):
        return self.references 
    @property 
    def cliente(self):
        return self.cliente 
    @property 
    def tipo_Vehiculo(self):
        return self.tipo_Vehiculo 
    @property 
    def num_Vehiculo(self):
        return self.num_Vehiculo 
    @property 
    def Status(self):
        return self.Status 
    @property 
    def scac(self):
        return self.scac 
    @property 
    def tod_Fecha(self):
        return self.tod_Fecha 
    @property 
    def tod_Time(self):
        return self.tod_Time 
    @property 
    def tnf_Fecha(self):
        return self.tnf_Fecha 
    @property 
    def tnf_Time(self):
        return self.tnf_Time 
    @property 
    def dxs_Fecha(self):
        return self.dxs_Fecha 
    @property 
    def dxs_Time(self):
        return self.dxs_Time 
    @property 
    def dly_Fecha(self):
        return self.dly_Fecha 
    @property 
    def dly_Time(self):
        return self.dly_Time 
    @property 
    def dly_Notes(self):
        return self.dly_Notes 
    @property 
    def afs_Fecha(self):
        return self.afs_Fecha 
    @property 
    def afs_Time(self):
        return self.afs_Time 
    @property 
    def dpu_Fecha(self):
        return self.dpu_Fecha 
    @property 
    def dpu_Time(self):
        return self.dpu_Time 
    @property 
    def exr_Fecha(self):
        return self.exr_Fecha 
    @property 
    def exr_Time(self):
        return self.exr_Time 
    @property 
    def exr_Notes(self):
        return self.exr_Notes 
    @property 
    def ecc_Fecha(self):
        return self.ecc_Fecha 
    @property 
    def ecc_Time(self):
        return self.ecc_Time 
    @property 
    def ilr_Fecha(self):
        return self.ilr_Fecha 
    @property 
    def ilr_Time(self):
        return self.ilr_Time 
    @property 
    def ilr_Tipo(self):
        return self.ilr_Tipo 
    @property 
    def ilr_Notes(self):
        return self.ilr_Notes 
    @property 
    def clr_Fecha(self):
        return self.clr_Fecha 
    @property 
    def clr_Time(self):
        return self.clr_Time 
    @property 
    def st1_Fecha(self):
        return self.st1_Fecha 
    @property 
    def st1_Time(self):
        return self.st1_Time 
    @property 
    def st1_Notes(self):
        return self.st1_Notes 
    @property 
    def tsc_Time(self):
        return self.tsc_Time 
    @property 
    def tsc_Fecha(self):
        return self.tsc_Fecha 
    @property 
    def tsc_Notes(self):
        return self.tsc_Notes 
    
    @references.setter
    def references(self,value):
        self._references = value
    @cliente.setter
    def cliente(self,value):
        self._cliente = value
    @tipo_Vehiculo.setter
    def tipo_Vehiculo(self,value):
        self._tipo_Vehiculo = value
    @num_Vehiculo.setter
    def num_Vehiculo(self,value):
        self._num_Vehiculo = value
    @Status.setter
    def Status(self,value):
        self._Status = value
    @scac.setter
    def scac(self,value):
        self._scac = value
    @tod_Fecha.setter
    def tod_Fecha(self,value):
        self._tod_Fecha = value
    @tod_Time.setter
    def tod_Time(self,value):
        self._tod_Time = value
    @tnf_Fecha.setter
    def tnf_Fecha(self,value):
        self._tnf_Fecha = value
    @tnf_Time.setter
    def tnf_Time(self,value):
        self._tnf_Time = value
    @dxs_Fecha.setter
    def dxs_Fecha(self,value):
        self._dxs_Fecha = value
    @dxs_Time.setter
    def dxs_Time(self,value):
        self._dxs_Time = value
    @dly_Fecha.setter
    def dly_Fecha(self,value):
        self._dly_Fecha = value
    @dly_Time.setter
    def dly_Time(self,value):
        self._dly_Time = value
    @dly_Notes.setter
    def dly_Notes(self,value):
        self._dly_Notes = value
    @afs_Fecha.setter
    def afs_Fecha(self,value):
        self._afs_Fecha = value
    @afs_Time.setter
    def afs_Time(self,value):
        self._afs_Time = value
    @dpu_Fecha.setter
    def dpu_Fecha(self,value):
        self._dpu_Fecha = value
    @dpu_Time.setter
    def dpu_Time(self,value):
        self._dpu_Time = value
    @exr_Fecha.setter
    def exr_Fecha(self,value):
        self._exr_Fecha = value
    @exr_Time.setter
    def exr_Time(self,value):
        self._exr_Time = value
    @exr_Notes.setter
    def exr_Notes(self,value):
        self._exr_Notes = value
    @ecc_Fecha.setter
    def ecc_Fecha(self,value):
        self._ecc_Fecha = value
    @ecc_Time.setter
    def ecc_Time(self,value):
        self._ecc_Time = value
    @ilr_Fecha.setter
    def ilr_Fecha(self,value):
        self._ilr_Fecha = value
    @ilr_Time.setter
    def ilr_Time(self,value):
        self._ilr_Time = value
    @ilr_Tipo.setter
    def ilr_Tipo(self,value):
        self._ilr_Tipo = value
    @ilr_Notes.setter
    def ilr_Notes(self,value):
        self._ilr_Notes = value
    @clr_Fecha.setter
    def clr_Fecha(self,value):
        self._clr_Fecha = value
    @clr_Time.setter
    def clr_Time(self,value):
        self._clr_Time = value
    @st1_Fecha.setter
    def st1_Fecha(self,value):
        self._st1_Fecha = value
    @st1_Time.setter
    def st1_Time(self,value):
        self._st1_Time = value
    @st1_Notes.setter
    def st1_Notes(self,value):
        self._st1_Notes = value
    @tsc_Time.setter
    def tsc_Time(self,value):
        self._tsc_Time = value
    @tsc_Fecha.setter
    def tsc_Fecha(self,value):
        self._tsc_Fecha = value
    @tsc_Notes.setter
    def tsc_Notes(self,value):
        self._tsc_Notes = value