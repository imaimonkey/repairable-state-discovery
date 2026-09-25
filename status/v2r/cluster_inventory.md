# V2R cluster inventory

2026-09-25T13:23:39.738159+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319112978432 available bytes; 82.20% used; 112477583 free inodes.

server1 `/home`: 319112978432 available bytes; 82.20% used; 112477583 free inodes.

server1 `/tmp`: 319112978432 available bytes; 82.20% used; 112477583 free inodes.

server1 `/var/tmp`: 319112978432 available bytes; 82.20% used; 112477583 free inodes.

server1 `/mnt/raid5`: 364247527424 available bytes; 98.33% used; 337547858 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 18294661120 available bytes; 98.98% used; 110408759 free inodes.

server2 `/home`: 18294661120 available bytes; 98.98% used; 110408759 free inodes.

server2 `/tmp`: 18294661120 available bytes; 98.98% used; 110408759 free inodes.

server2 `/var/tmp`: 18294661120 available bytes; 98.98% used; 110408759 free inodes.

server2 `/mnt/raid5`: 323639767040 available bytes; 97.76% used; 445077115 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84198162432 available bytes; 95.30% used; 114154966 free inodes.

server3 `/home`: 84198162432 available bytes; 95.30% used; 114154966 free inodes.

server3 `/data`: 142348173312 available bytes; 98.03% used; 225809817 free inodes.

server3 `/tmp`: 84198162432 available bytes; 95.30% used; 114154966 free inodes.

server3 `/var/tmp`: 84198162432 available bytes; 95.30% used; 114154966 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656135680 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656135680 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231409913856 available bytes; 96.80% used; 224952599 free inodes.

server4 `/tmp`: 105656135680 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656135680 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
