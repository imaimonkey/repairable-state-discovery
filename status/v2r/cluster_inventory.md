# V2R cluster inventory

2026-09-24T17:29:08.709777+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324004720640 available bytes; 81.92% used; 112481444 free inodes.

server1 `/home`: 324004720640 available bytes; 81.92% used; 112481444 free inodes.

server1 `/tmp`: 324004720640 available bytes; 81.92% used; 112481444 free inodes.

server1 `/var/tmp`: 324004720640 available bytes; 81.92% used; 112481444 free inodes.

server1 `/mnt/raid5`: 416450023424 available bytes; 98.09% used; 337646494 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 56925483008 available bytes; 96.82% used; 110412934 free inodes.

server2 `/home`: 56925483008 available bytes; 96.82% used; 110412934 free inodes.

server2 `/tmp`: 56925483008 available bytes; 96.82% used; 110412934 free inodes.

server2 `/var/tmp`: 56925483008 available bytes; 96.82% used; 110412934 free inodes.

server2 `/mnt/raid5`: 498847490048 available bytes; 96.55% used; 445162609 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84411645952 available bytes; 95.29% used; 114156148 free inodes.

server3 `/home`: 84411645952 available bytes; 95.29% used; 114156148 free inodes.

server3 `/data`: 158947532800 available bytes; 97.80% used; 225786857 free inodes.

server3 `/tmp`: 84411645952 available bytes; 95.29% used; 114156148 free inodes.

server3 `/var/tmp`: 84411645952 available bytes; 95.29% used; 114156148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105681575936 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105681575936 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 89075167232 available bytes; 98.77% used; 225254150 free inodes.

server4 `/tmp`: 105681575936 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105681575936 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
