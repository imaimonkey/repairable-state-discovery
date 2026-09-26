# V2R cluster inventory

2026-09-26T07:15:50.979214+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318769098752 available bytes; 82.22% used; 112476295 free inodes.

server1 `/home`: 318769098752 available bytes; 82.22% used; 112476295 free inodes.

server1 `/tmp`: 318769098752 available bytes; 82.22% used; 112476295 free inodes.

server1 `/var/tmp`: 318769098752 available bytes; 82.22% used; 112476295 free inodes.

server1 `/mnt/raid5`: 219273928704 available bytes; 98.99% used; 337539321 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22322008064 available bytes; 98.75% used; 110403882 free inodes.

server2 `/home`: 22322008064 available bytes; 98.75% used; 110403882 free inodes.

server2 `/tmp`: 22322008064 available bytes; 98.75% used; 110403882 free inodes.

server2 `/var/tmp`: 22322008064 available bytes; 98.75% used; 110403882 free inodes.

server2 `/mnt/raid5`: 271666130944 available bytes; 98.12% used; 445027447 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82677846016 available bytes; 95.39% used; 114110897 free inodes.

server3 `/home`: 82677846016 available bytes; 95.39% used; 114110897 free inodes.

server3 `/data`: 123983368192 available bytes; 98.29% used; 225821307 free inodes.

server3 `/tmp`: 82677846016 available bytes; 95.39% used; 114110897 free inodes.

server3 `/var/tmp`: 82677846016 available bytes; 95.39% used; 114110897 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106074877952 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106074877952 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105876426752 available bytes; 98.54% used; 224922737 free inodes.

server4 `/tmp`: 106074877952 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106074877952 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
