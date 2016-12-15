
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import filter_change_update_delay
class hide_filter_change_update_delay_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-filter-change-update-delay-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__filter_change_update_delay',)

  _yang_name = 'hide-filter-change-update-delay-holder'
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
    self.__filter_change_update_delay = YANGDynClass(base=YANGListType("filter_delay_value",filter_change_update_delay.filter_change_update_delay, yang_name="filter-change-update-delay", rest_name="filter-change-update-delay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='filter-delay-value', extensions={u'tailf-common': {u'info': u'Change filter change update delay timer', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'57', u'cli-suppress-key-abbreviation': None, u'callpoint': u'filterChangeUpdateDelay'}}), is_container='list', yang_name="filter-change-update-delay", rest_name="filter-change-update-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Change filter change update delay timer', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'57', u'cli-suppress-key-abbreviation': None, u'callpoint': u'filterChangeUpdateDelay'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

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
      return [u'hide-filter-change-update-delay-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_filter_change_update_delay(self):
    """
    Getter method for filter_change_update_delay, mapped from YANG variable /hide_filter_change_update_delay_holder/filter_change_update_delay (list)

    YANG Description: Change filter change update delay timer
    """
    return self.__filter_change_update_delay
      
  def _set_filter_change_update_delay(self, v, load=False):
    """
    Setter method for filter_change_update_delay, mapped from YANG variable /hide_filter_change_update_delay_holder/filter_change_update_delay (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter_change_update_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter_change_update_delay() directly.

    YANG Description: Change filter change update delay timer
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("filter_delay_value",filter_change_update_delay.filter_change_update_delay, yang_name="filter-change-update-delay", rest_name="filter-change-update-delay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='filter-delay-value', extensions={u'tailf-common': {u'info': u'Change filter change update delay timer', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'57', u'cli-suppress-key-abbreviation': None, u'callpoint': u'filterChangeUpdateDelay'}}), is_container='list', yang_name="filter-change-update-delay", rest_name="filter-change-update-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Change filter change update delay timer', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'57', u'cli-suppress-key-abbreviation': None, u'callpoint': u'filterChangeUpdateDelay'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter_change_update_delay must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("filter_delay_value",filter_change_update_delay.filter_change_update_delay, yang_name="filter-change-update-delay", rest_name="filter-change-update-delay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='filter-delay-value', extensions={u'tailf-common': {u'info': u'Change filter change update delay timer', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'57', u'cli-suppress-key-abbreviation': None, u'callpoint': u'filterChangeUpdateDelay'}}), is_container='list', yang_name="filter-change-update-delay", rest_name="filter-change-update-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Change filter change update delay timer', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'57', u'cli-suppress-key-abbreviation': None, u'callpoint': u'filterChangeUpdateDelay'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)""",
        })

    self.__filter_change_update_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter_change_update_delay(self):
    self.__filter_change_update_delay = YANGDynClass(base=YANGListType("filter_delay_value",filter_change_update_delay.filter_change_update_delay, yang_name="filter-change-update-delay", rest_name="filter-change-update-delay", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='filter-delay-value', extensions={u'tailf-common': {u'info': u'Change filter change update delay timer', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'57', u'cli-suppress-key-abbreviation': None, u'callpoint': u'filterChangeUpdateDelay'}}), is_container='list', yang_name="filter-change-update-delay", rest_name="filter-change-update-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Change filter change update delay timer', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'57', u'cli-suppress-key-abbreviation': None, u'callpoint': u'filterChangeUpdateDelay'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

  filter_change_update_delay = __builtin__.property(_get_filter_change_update_delay, _set_filter_change_update_delay)


  _pyangbind_elements = {'filter_change_update_delay': filter_change_update_delay, }


