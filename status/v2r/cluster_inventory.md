# V2R cluster inventory

2026-09-27T03:57:50.234310+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315074813952 available bytes; 82.42% used; 112443035 free inodes.

server1 `/home`: 315074813952 available bytes; 82.42% used; 112443035 free inodes.

server1 `/tmp`: 315074813952 available bytes; 82.42% used; 112443035 free inodes.

server1 `/var/tmp`: 315074813952 available bytes; 82.42% used; 112443035 free inodes.

server1 `/mnt/raid5`: 636785090560 available bytes; 97.08% used; 337401379 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17623973888 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17623973888 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17623973888 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17623973888 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 577382629376 available bytes; 96.01% used; 444882935 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78696693760 available bytes; 95.61% used; 114062929 free inodes.

server3 `/home`: 78696693760 available bytes; 95.61% used; 114062929 free inodes.

server3 `/data`: 1335221014528 available bytes; 81.55% used; 225759923 free inodes.

server3 `/tmp`: 78696693760 available bytes; 95.61% used; 114062929 free inodes.

server3 `/var/tmp`: 78696693760 available bytes; 95.61% used; 114062929 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111027318784 available bytes; 93.80% used; 114372943 free inodes.

server4 `/home`: 111027318784 available bytes; 93.80% used; 114372943 free inodes.

server4 `/data`: 382178369536 available bytes; 94.72% used; 224780793 free inodes.

server4 `/tmp`: 111027318784 available bytes; 93.80% used; 114372943 free inodes.

server4 `/var/tmp`: 111027318784 available bytes; 93.80% used; 114372943 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
