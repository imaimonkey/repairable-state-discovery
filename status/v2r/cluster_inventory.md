# V2R cluster inventory

2026-09-25T14:43:08.256652+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319159181312 available bytes; 82.20% used; 112476978 free inodes.

server1 `/home`: 319159181312 available bytes; 82.20% used; 112476978 free inodes.

server1 `/tmp`: 319159181312 available bytes; 82.20% used; 112476978 free inodes.

server1 `/var/tmp`: 319159181312 available bytes; 82.20% used; 112476978 free inodes.

server1 `/mnt/raid5`: 364430290944 available bytes; 98.33% used; 337546788 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 12797571072 available bytes; 99.29% used; 110407859 free inodes.

server2 `/home`: 12797571072 available bytes; 99.29% used; 110407859 free inodes.

server2 `/tmp`: 12797571072 available bytes; 99.29% used; 110407859 free inodes.

server2 `/var/tmp`: 12797571072 available bytes; 99.29% used; 110407859 free inodes.

server2 `/mnt/raid5`: 321215352832 available bytes; 97.78% used; 445074524 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84265156608 available bytes; 95.30% used; 114154470 free inodes.

server3 `/home`: 84265156608 available bytes; 95.30% used; 114154470 free inodes.

server3 `/data`: 142200602624 available bytes; 98.03% used; 225808483 free inodes.

server3 `/tmp`: 84265156608 available bytes; 95.30% used; 114154470 free inodes.

server3 `/var/tmp`: 84265156608 available bytes; 95.30% used; 114154470 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654005760 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105654005760 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231429128192 available bytes; 96.80% used; 224945844 free inodes.

server4 `/tmp`: 105654005760 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105654005760 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
