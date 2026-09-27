# V2R cluster inventory

2026-09-27T09:39:02.634346+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314450186240 available bytes; 82.46% used; 112440735 free inodes.

server1 `/home`: 314450186240 available bytes; 82.46% used; 112440735 free inodes.

server1 `/tmp`: 314450186240 available bytes; 82.46% used; 112440735 free inodes.

server1 `/var/tmp`: 314450186240 available bytes; 82.46% used; 112440735 free inodes.

server1 `/mnt/raid5`: 635450593280 available bytes; 97.08% used; 337424409 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16507764736 available bytes; 99.08% used; 110356914 free inodes.

server2 `/home`: 16507764736 available bytes; 99.08% used; 110356914 free inodes.

server2 `/tmp`: 16507764736 available bytes; 99.08% used; 110356914 free inodes.

server2 `/var/tmp`: 16507764736 available bytes; 99.08% used; 110356914 free inodes.

server2 `/mnt/raid5`: 573374578688 available bytes; 96.04% used; 444741306 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78548312064 available bytes; 95.62% used; 114062912 free inodes.

server3 `/home`: 78548312064 available bytes; 95.62% used; 114062912 free inodes.

server3 `/data`: 1332473520128 available bytes; 81.58% used; 225762205 free inodes.

server3 `/tmp`: 78548312064 available bytes; 95.62% used; 114062912 free inodes.

server3 `/var/tmp`: 78548312064 available bytes; 95.62% used; 114062912 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111050162176 available bytes; 93.80% used; 114372850 free inodes.

server4 `/home`: 111050162176 available bytes; 93.80% used; 114372850 free inodes.

server4 `/data`: 364005548032 available bytes; 94.97% used; 224767153 free inodes.

server4 `/tmp`: 111050162176 available bytes; 93.80% used; 114372850 free inodes.

server4 `/var/tmp`: 111050162176 available bytes; 93.80% used; 114372850 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
