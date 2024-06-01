alert_dict = {
    'SRV HUAWEI (iBMC)': {
        1: 'Communication between the iBMC and PCIe card 3 (RAID) failed',
        2: 'Communication between the iBMC and PCIe card 5 (9460-8i) failed',
        3: 'Communication between the iBMC and PCIe card 5 (RAID) failed',
        4: 'DIMM050 triggered an uncorrectable error',
        5: 'Failed RAID array detected',
        6: 'The disk Disk0 failure',
        7: 'The disk Disk14 failure',
        8: 'The disk M.2 Disk1(PCIe4) is missing',
        9: 'The disk M.2 Disk1(PCIe4) RAID array is invalid',
        10: 'The logical drive 0 under RAID card PCIe Card 4 (RAID) is degraded'
    },
    'SRV DELL (IDRAC)': {
        1: 'Chassis management controller (CMC) redundancy is lost',
        2: 'CMC Fan Status Error',
        3: 'Correctable Machine Check Exception detected on CPU 2',
        4: 'Correctable memory error logging disabled for a memory device at location DIMM_B1',
        5: 'Internal Storage Enclosure Device Failure (Bay 1, Box 1, Port 1I, Slot 0)',
        6: 'Power supply redundancy is lost',
        7: 'The power input for power supply 1 is lost',
        8: 'The Power Supply Unit (PSU) 1 is not receiving input power because of issues in PSU or cable connections',
        9: 'The watchdog timer reset the system',
        10: 'The CMOS battery is low'
    },
    'SRV HPE (iLO)': {
        1: 'Cache Module Status Degraded',
        2: 'High rate of corrected memory errors, performance may be degraded (Processor 1, DIMM 3).',
        3: 'Internal Storage Enclosure Device Failure (Bay 6, Box 1, Port 1I, Slot 0)',
        4: 'Logical Drive 02 Status Degraded (Transforming)',
        5: 'The disk Disk14 state is abnormal',
        6: 'Redundancy status changed to decreased by adapter in slot 2, port 1',
        7: 'Uncorrectable Memory Error ((Processor 2, Memory Module 9))',
        8: 'The watchdog timer reset the system',
        9: 'The power input for power supply 2 is lost',
        10: 'The CMOS battery is low'
    }
}
