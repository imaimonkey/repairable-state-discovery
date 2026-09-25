# V2R cluster inventory

2026-09-25T11:57:56.647266+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319045713920 available bytes; 82.20% used; 112478827 free inodes.

server1 `/home`: 319045713920 available bytes; 82.20% used; 112478827 free inodes.

server1 `/tmp`: 319045713920 available bytes; 82.20% used; 112478827 free inodes.

server1 `/var/tmp`: 319045713920 available bytes; 82.20% used; 112478827 free inodes.

server1 `/mnt/raid5`: 364332228608 available bytes; 98.33% used; 337549116 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22911434752 available bytes; 98.72% used; 110409974 free inodes.

server2 `/home`: 22911434752 available bytes; 98.72% used; 110409974 free inodes.

server2 `/tmp`: 22911434752 available bytes; 98.72% used; 110409974 free inodes.

server2 `/var/tmp`: 22911434752 available bytes; 98.72% used; 110409974 free inodes.

server2 `/mnt/raid5`: 326107066368 available bytes; 97.75% used; 445082237 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84216274944 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84216274944 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142122164224 available bytes; 98.04% used; 225812668 free inodes.

server3 `/tmp`: 84216274944 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84216274944 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105593860096 available bytes; 94.11% used; 114350234 free inodes.

server4 `/home`: 105593860096 available bytes; 94.11% used; 114350234 free inodes.

server4 `/data`: 232650153984 available bytes; 96.78% used; 224973058 free inodes.

server4 `/tmp`: 105593860096 available bytes; 94.11% used; 114350234 free inodes.

server4 `/var/tmp`: 105593860096 available bytes; 94.11% used; 114350234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
