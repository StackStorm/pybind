
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bna_config_cmd
import bna_config_cmd_status
class brocade_ras(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras - based on the path /brocade_ras_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an instrumentation to log collection 
 like supportsave,copy support and USB management
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bna_config_cmd','__bna_config_cmd_status',)

  _yang_name = 'brocade-ras'
  _rest_name = ''

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__bna_config_cmd = YANGDynClass(base=bna_config_cmd.bna_config_cmd, is_leaf=True, yang_name="bna-config-cmd", rest_name="bna-config-cmd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='rpc', is_config=True)
    self.__bna_config_cmd_status = YANGDynClass(base=bna_config_cmd_status.bna_config_cmd_status, is_leaf=True, yang_name="bna-config-cmd-status", rest_name="bna-config-cmd-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='rpc', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'brocade_ras_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_bna_config_cmd(self):
    """
    Getter method for bna_config_cmd, mapped from YANG variable /brocade_ras_rpc/bna_config_cmd (rpc)

    YANG Description: copy configuration data to/from system. This is a non-blocking command, the caller needs to query for the command completion status using the session-id returned.
    """
    return self.__bna_config_cmd
      
  def _set_bna_config_cmd(self, v, load=False):
    """
    Setter method for bna_config_cmd, mapped from YANG variable /brocade_ras_rpc/bna_config_cmd (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bna_config_cmd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bna_config_cmd() directly.

    YANG Description: copy configuration data to/from system. This is a non-blocking command, the caller needs to query for the command completion status using the session-id returned.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bna_config_cmd.bna_config_cmd, is_leaf=True, yang_name="bna-config-cmd", rest_name="bna-config-cmd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bna_config_cmd must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=bna_config_cmd.bna_config_cmd, is_leaf=True, yang_name="bna-config-cmd", rest_name="bna-config-cmd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='rpc', is_config=True)""",
        })

    self.__bna_config_cmd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bna_config_cmd(self):
    self.__bna_config_cmd = YANGDynClass(base=bna_config_cmd.bna_config_cmd, is_leaf=True, yang_name="bna-config-cmd", rest_name="bna-config-cmd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='rpc', is_config=True)


  def _get_bna_config_cmd_status(self):
    """
    Getter method for bna_config_cmd_status, mapped from YANG variable /brocade_ras_rpc/bna_config_cmd_status (rpc)

    YANG Description: Query the status of a previous config-cmd
    """
    return self.__bna_config_cmd_status
      
  def _set_bna_config_cmd_status(self, v, load=False):
    """
    Setter method for bna_config_cmd_status, mapped from YANG variable /brocade_ras_rpc/bna_config_cmd_status (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bna_config_cmd_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bna_config_cmd_status() directly.

    YANG Description: Query the status of a previous config-cmd
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bna_config_cmd_status.bna_config_cmd_status, is_leaf=True, yang_name="bna-config-cmd-status", rest_name="bna-config-cmd-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bna_config_cmd_status must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=bna_config_cmd_status.bna_config_cmd_status, is_leaf=True, yang_name="bna-config-cmd-status", rest_name="bna-config-cmd-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='rpc', is_config=True)""",
        })

    self.__bna_config_cmd_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bna_config_cmd_status(self):
    self.__bna_config_cmd_status = YANGDynClass(base=bna_config_cmd_status.bna_config_cmd_status, is_leaf=True, yang_name="bna-config-cmd-status", rest_name="bna-config-cmd-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='rpc', is_config=True)

  bna_config_cmd = __builtin__.property(_get_bna_config_cmd, _set_bna_config_cmd)
  bna_config_cmd_status = __builtin__.property(_get_bna_config_cmd_status, _set_bna_config_cmd_status)


  _pyangbind_elements = {'bna_config_cmd': bna_config_cmd, 'bna_config_cmd_status': bna_config_cmd_status, }

