# V2R cluster inventory

2026-09-25T05:37:44.651406+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318873038848 available bytes; 82.21% used; 112480333 free inodes.

server1 `/home`: 318873038848 available bytes; 82.21% used; 112480333 free inodes.

server1 `/tmp`: 318873038848 available bytes; 82.21% used; 112480333 free inodes.

server1 `/var/tmp`: 318873038848 available bytes; 82.21% used; 112480333 free inodes.

server1 `/mnt/raid5`: 408471044096 available bytes; 98.13% used; 337567350 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22919016448 available bytes; 98.72% used; 110410443 free inodes.

server2 `/home`: 22919016448 available bytes; 98.72% used; 110410443 free inodes.

server2 `/tmp`: 22919016448 available bytes; 98.72% used; 110410443 free inodes.

server2 `/var/tmp`: 22919016448 available bytes; 98.72% used; 110410443 free inodes.

server2 `/mnt/raid5`: 461219119104 available bytes; 96.81% used; 445103010 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84313583616 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84313583616 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142776680448 available bytes; 98.03% used; 225814694 free inodes.

server3 `/tmp`: 84313583616 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84313583616 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105649774592 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105649774592 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 26384838656 available bytes; 99.64% used; 224967036 free inodes.

server4 `/tmp`: 105649774592 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105649774592 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
