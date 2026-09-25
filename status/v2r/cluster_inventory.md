# V2R cluster inventory

2026-09-25T11:15:08.170920+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319061581824 available bytes; 82.20% used; 112478867 free inodes.

server1 `/home`: 319061581824 available bytes; 82.20% used; 112478867 free inodes.

server1 `/tmp`: 319061581824 available bytes; 82.20% used; 112478867 free inodes.

server1 `/var/tmp`: 319061581824 available bytes; 82.20% used; 112478867 free inodes.

server1 `/mnt/raid5`: 370028048384 available bytes; 98.30% used; 337554644 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22907498496 available bytes; 98.72% used; 110409990 free inodes.

server2 `/home`: 22907498496 available bytes; 98.72% used; 110409990 free inodes.

server2 `/tmp`: 22907498496 available bytes; 98.72% used; 110409990 free inodes.

server2 `/var/tmp`: 22907498496 available bytes; 98.72% used; 110409990 free inodes.

server2 `/mnt/raid5`: 328651476992 available bytes; 97.73% used; 445088457 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84140027904 available bytes; 95.30% used; 114155492 free inodes.

server3 `/home`: 84140027904 available bytes; 95.30% used; 114155492 free inodes.

server3 `/data`: 142084280320 available bytes; 98.04% used; 225814444 free inodes.

server3 `/tmp`: 84140027904 available bytes; 95.30% used; 114155492 free inodes.

server3 `/var/tmp`: 84140027904 available bytes; 95.30% used; 114155492 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105612021760 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105612021760 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238634532864 available bytes; 96.70% used; 224981907 free inodes.

server4 `/tmp`: 105612021760 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105612021760 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
