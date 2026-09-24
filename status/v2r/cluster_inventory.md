# V2R cluster inventory

2026-09-24T03:46:50.278264+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324741259264 available bytes; 81.88% used; 112493725 free inodes.

server1 `/home`: 324741259264 available bytes; 81.88% used; 112493725 free inodes.

server1 `/tmp`: 324741259264 available bytes; 81.88% used; 112493725 free inodes.

server1 `/var/tmp`: 324741259264 available bytes; 81.88% used; 112493725 free inodes.

server1 `/mnt/raid5`: 406964895744 available bytes; 98.13% used; 337724824 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40819920896 available bytes; 97.72% used; 110430972 free inodes.

server2 `/home`: 40819920896 available bytes; 97.72% used; 110430972 free inodes.

server2 `/tmp`: 40819920896 available bytes; 97.72% used; 110430972 free inodes.

server2 `/var/tmp`: 40819920896 available bytes; 97.72% used; 110430972 free inodes.

server2 `/mnt/raid5`: 526702628864 available bytes; 96.36% used; 445197299 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292366807040 available bytes; 83.68% used; 114198300 free inodes.

server3 `/home`: 292366807040 available bytes; 83.68% used; 114198300 free inodes.

server3 `/data`: 33878675456 available bytes; 99.53% used; 225842668 free inodes.

server3 `/tmp`: 292366807040 available bytes; 83.68% used; 114198300 free inodes.

server3 `/var/tmp`: 292366807040 available bytes; 83.68% used; 114198300 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105792737280 available bytes; 94.10% used; 114349566 free inodes.

server4 `/home`: 105792737280 available bytes; 94.10% used; 114349566 free inodes.

server4 `/data`: 276616130560 available bytes; 96.18% used; 225384210 free inodes.

server4 `/tmp`: 105792737280 available bytes; 94.10% used; 114349566 free inodes.

server4 `/var/tmp`: 105792737280 available bytes; 94.10% used; 114349566 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
