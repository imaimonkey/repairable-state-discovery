# V2R cluster inventory

2026-09-26T10:52:31.050662+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318213332992 available bytes; 82.25% used; 112474817 free inodes.

server1 `/home`: 318213332992 available bytes; 82.25% used; 112474817 free inodes.

server1 `/tmp`: 318213332992 available bytes; 82.25% used; 112474817 free inodes.

server1 `/var/tmp`: 318213332992 available bytes; 82.25% used; 112474817 free inodes.

server1 `/mnt/raid5`: 218780422144 available bytes; 99.00% used; 337538253 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19844943872 available bytes; 98.89% used; 110384887 free inodes.

server2 `/home`: 19844943872 available bytes; 98.89% used; 110384887 free inodes.

server2 `/tmp`: 19844943872 available bytes; 98.89% used; 110384887 free inodes.

server2 `/var/tmp`: 19844943872 available bytes; 98.89% used; 110384887 free inodes.

server2 `/mnt/raid5`: 241462542336 available bytes; 98.33% used; 444978714 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82658914304 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82658914304 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123570888704 available bytes; 98.29% used; 225826152 free inodes.

server3 `/tmp`: 82658914304 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82658914304 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['1', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105926897664 available bytes; 94.09% used; 114347976 free inodes.

server4 `/home`: 105926897664 available bytes; 94.09% used; 114347976 free inodes.

server4 `/data`: 88989663232 available bytes; 98.77% used; 224880591 free inodes.

server4 `/tmp`: 105926897664 available bytes; 94.09% used; 114347976 free inodes.

server4 `/var/tmp`: 105926897664 available bytes; 94.09% used; 114347976 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
