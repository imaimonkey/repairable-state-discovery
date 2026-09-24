# V2R cluster inventory

2026-09-24T04:32:46.589681+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324632526848 available bytes; 81.89% used; 112492984 free inodes.

server1 `/home`: 324632526848 available bytes; 81.89% used; 112492984 free inodes.

server1 `/tmp`: 324632526848 available bytes; 81.89% used; 112492984 free inodes.

server1 `/var/tmp`: 324632526848 available bytes; 81.89% used; 112492984 free inodes.

server1 `/mnt/raid5`: 450480574464 available bytes; 97.93% used; 337724666 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40781045760 available bytes; 97.72% used; 110430524 free inodes.

server2 `/home`: 40781045760 available bytes; 97.72% used; 110430524 free inodes.

server2 `/tmp`: 40781045760 available bytes; 97.72% used; 110430524 free inodes.

server2 `/var/tmp`: 40781045760 available bytes; 97.72% used; 110430524 free inodes.

server2 `/mnt/raid5`: 525264080896 available bytes; 96.37% used; 445195893 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292003815424 available bytes; 83.71% used; 114176144 free inodes.

server3 `/home`: 292003815424 available bytes; 83.71% used; 114176144 free inodes.

server3 `/data`: 24382570496 available bytes; 99.66% used; 225840889 free inodes.

server3 `/tmp`: 292003815424 available bytes; 83.71% used; 114176144 free inodes.

server3 `/var/tmp`: 292003815424 available bytes; 83.71% used; 114176144 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105844338688 available bytes; 94.09% used; 114349416 free inodes.

server4 `/home`: 105844338688 available bytes; 94.09% used; 114349416 free inodes.

server4 `/data`: 253406425088 available bytes; 96.50% used; 225366897 free inodes.

server4 `/tmp`: 105844338688 available bytes; 94.09% used; 114349416 free inodes.

server4 `/var/tmp`: 105844338688 available bytes; 94.09% used; 114349416 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
