# V2R cluster inventory

2026-09-25T13:37:24.084779+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319182327808 available bytes; 82.19% used; 112477030 free inodes.

server1 `/home`: 319182327808 available bytes; 82.19% used; 112477030 free inodes.

server1 `/tmp`: 319182327808 available bytes; 82.19% used; 112477030 free inodes.

server1 `/var/tmp`: 319182327808 available bytes; 82.19% used; 112477030 free inodes.

server1 `/mnt/raid5`: 364189646848 available bytes; 98.33% used; 337547725 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 16534310912 available bytes; 99.08% used; 110408646 free inodes.

server2 `/home`: 16534310912 available bytes; 99.08% used; 110408646 free inodes.

server2 `/tmp`: 16534310912 available bytes; 99.08% used; 110408646 free inodes.

server2 `/var/tmp`: 16534310912 available bytes; 99.08% used; 110408646 free inodes.

server2 `/mnt/raid5`: 323256967168 available bytes; 97.77% used; 445077243 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84280987648 available bytes; 95.30% used; 114154461 free inodes.

server3 `/home`: 84280987648 available bytes; 95.30% used; 114154461 free inodes.

server3 `/data`: 142350577664 available bytes; 98.03% used; 225809569 free inodes.

server3 `/tmp`: 84280987648 available bytes; 95.30% used; 114154461 free inodes.

server3 `/var/tmp`: 84280987648 available bytes; 95.30% used; 114154461 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655791616 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655791616 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231394082816 available bytes; 96.80% used; 224951171 free inodes.

server4 `/tmp`: 105655791616 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655791616 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
