# V2R cluster inventory

2026-09-25T11:19:43.098244+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063855104 available bytes; 82.20% used; 112478865 free inodes.

server1 `/home`: 319063855104 available bytes; 82.20% used; 112478865 free inodes.

server1 `/tmp`: 319063855104 available bytes; 82.20% used; 112478865 free inodes.

server1 `/var/tmp`: 319063855104 available bytes; 82.20% used; 112478865 free inodes.

server1 `/mnt/raid5`: 364169781248 available bytes; 98.33% used; 337550311 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22905626624 available bytes; 98.72% used; 110409976 free inodes.

server2 `/home`: 22905626624 available bytes; 98.72% used; 110409976 free inodes.

server2 `/tmp`: 22905626624 available bytes; 98.72% used; 110409976 free inodes.

server2 `/var/tmp`: 22905626624 available bytes; 98.72% used; 110409976 free inodes.

server2 `/mnt/raid5`: 327860404224 available bytes; 97.73% used; 445084057 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84141182976 available bytes; 95.30% used; 114155498 free inodes.

server3 `/home`: 84141182976 available bytes; 95.30% used; 114155498 free inodes.

server3 `/data`: 142087438336 available bytes; 98.04% used; 225814374 free inodes.

server3 `/tmp`: 84141182976 available bytes; 95.30% used; 114155498 free inodes.

server3 `/var/tmp`: 84141182976 available bytes; 95.30% used; 114155498 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105611902976 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105611902976 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238630670336 available bytes; 96.70% used; 224981330 free inodes.

server4 `/tmp`: 105611902976 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105611902976 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
