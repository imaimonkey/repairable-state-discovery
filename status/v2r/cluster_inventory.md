# V2R cluster inventory

2026-09-25T09:09:39.528707+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318836367360 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318836367360 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318836367360 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318836367360 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 350410604544 available bytes; 98.39% used; 337556961 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22839889920 available bytes; 98.73% used; 110410494 free inodes.

server2 `/home`: 22839889920 available bytes; 98.73% used; 110410494 free inodes.

server2 `/tmp`: 22839889920 available bytes; 98.73% used; 110410494 free inodes.

server2 `/var/tmp`: 22839889920 available bytes; 98.73% used; 110410494 free inodes.

server2 `/mnt/raid5`: 332289318912 available bytes; 97.70% used; 445092926 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84435599360 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84435599360 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142371770368 available bytes; 98.03% used; 225811010 free inodes.

server3 `/tmp`: 84435599360 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84435599360 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105632800768 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105632800768 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243369336832 available bytes; 96.64% used; 224998340 free inodes.

server4 `/tmp`: 105632800768 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105632800768 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
