# V2R cluster inventory

2026-09-24T13:26:29.125687+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324027150336 available bytes; 81.92% used; 112481517 free inodes.

server1 `/home`: 324027150336 available bytes; 81.92% used; 112481517 free inodes.

server1 `/tmp`: 324027150336 available bytes; 81.92% used; 112481517 free inodes.

server1 `/var/tmp`: 324027150336 available bytes; 81.92% used; 112481517 free inodes.

server1 `/mnt/raid5`: 417042501632 available bytes; 98.09% used; 337675626 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57534492672 available bytes; 96.79% used; 110428761 free inodes.

server2 `/home`: 57534492672 available bytes; 96.79% used; 110428761 free inodes.

server2 `/tmp`: 57534492672 available bytes; 96.79% used; 110428761 free inodes.

server2 `/var/tmp`: 57534492672 available bytes; 96.79% used; 110428761 free inodes.

server2 `/mnt/raid5`: 506755436544 available bytes; 96.50% used; 445169930 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84704006144 available bytes; 95.27% used; 114165487 free inodes.

server3 `/home`: 84704006144 available bytes; 95.27% used; 114165487 free inodes.

server3 `/data`: 161292566528 available bytes; 97.77% used; 225803238 free inodes.

server3 `/tmp`: 84704006144 available bytes; 95.27% used; 114165487 free inodes.

server3 `/var/tmp`: 84704006144 available bytes; 95.27% used; 114165487 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769889792 available bytes; 94.10% used; 114348745 free inodes.

server4 `/home`: 105769889792 available bytes; 94.10% used; 114348745 free inodes.

server4 `/data`: 90033774592 available bytes; 98.76% used; 225257178 free inodes.

server4 `/tmp`: 105769889792 available bytes; 94.10% used; 114348745 free inodes.

server4 `/var/tmp`: 105769889792 available bytes; 94.10% used; 114348745 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
