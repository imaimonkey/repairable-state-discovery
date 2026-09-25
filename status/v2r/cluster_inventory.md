# V2R cluster inventory

2026-09-25T11:45:42.148260+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319061168128 available bytes; 82.20% used; 112478831 free inodes.

server1 `/home`: 319061168128 available bytes; 82.20% used; 112478831 free inodes.

server1 `/tmp`: 319061168128 available bytes; 82.20% used; 112478831 free inodes.

server1 `/var/tmp`: 319061168128 available bytes; 82.20% used; 112478831 free inodes.

server1 `/mnt/raid5`: 364348809216 available bytes; 98.33% used; 337549174 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22905511936 available bytes; 98.72% used; 110409983 free inodes.

server2 `/home`: 22905511936 available bytes; 98.72% used; 110409983 free inodes.

server2 `/tmp`: 22905511936 available bytes; 98.72% used; 110409983 free inodes.

server2 `/var/tmp`: 22905511936 available bytes; 98.72% used; 110409983 free inodes.

server2 `/mnt/raid5`: 326648688640 available bytes; 97.74% used; 445082993 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 84213592064 available bytes; 95.30% used; 114155004 free inodes.

server3 `/home`: 84213592064 available bytes; 95.30% used; 114155004 free inodes.

server3 `/data`: 142043828224 available bytes; 98.04% used; 225813400 free inodes.

server3 `/tmp`: 84213592064 available bytes; 95.30% used; 114155004 free inodes.

server3 `/var/tmp`: 84213592064 available bytes; 95.30% used; 114155004 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105602707456 available bytes; 94.11% used; 114350248 free inodes.

server4 `/home`: 105602707456 available bytes; 94.11% used; 114350248 free inodes.

server4 `/data`: 232554504192 available bytes; 96.79% used; 224975541 free inodes.

server4 `/tmp`: 105602707456 available bytes; 94.11% used; 114350248 free inodes.

server4 `/var/tmp`: 105602707456 available bytes; 94.11% used; 114350248 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
