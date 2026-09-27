# V2R cluster inventory

2026-09-27T09:37:31.190897+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314450321408 available bytes; 82.46% used; 112440735 free inodes.

server1 `/home`: 314450321408 available bytes; 82.46% used; 112440735 free inodes.

server1 `/tmp`: 314450321408 available bytes; 82.46% used; 112440735 free inodes.

server1 `/var/tmp`: 314450321408 available bytes; 82.46% used; 112440735 free inodes.

server1 `/mnt/raid5`: 635451183104 available bytes; 97.08% used; 337424411 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16508448768 available bytes; 99.08% used; 110356964 free inodes.

server2 `/home`: 16508448768 available bytes; 99.08% used; 110356964 free inodes.

server2 `/tmp`: 16508448768 available bytes; 99.08% used; 110356964 free inodes.

server2 `/var/tmp`: 16508448768 available bytes; 99.08% used; 110356964 free inodes.

server2 `/mnt/raid5`: 573415559168 available bytes; 96.04% used; 444741463 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78547693568 available bytes; 95.62% used; 114062910 free inodes.

server3 `/home`: 78547693568 available bytes; 95.62% used; 114062910 free inodes.

server3 `/data`: 1332469678080 available bytes; 81.58% used; 225762223 free inodes.

server3 `/tmp`: 78547693568 available bytes; 95.62% used; 114062910 free inodes.

server3 `/var/tmp`: 78547693568 available bytes; 95.62% used; 114062910 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111050182656 available bytes; 93.80% used; 114372850 free inodes.

server4 `/home`: 111050182656 available bytes; 93.80% used; 114372850 free inodes.

server4 `/data`: 364005941248 available bytes; 94.97% used; 224767149 free inodes.

server4 `/tmp`: 111050182656 available bytes; 93.80% used; 114372850 free inodes.

server4 `/var/tmp`: 111050182656 available bytes; 93.80% used; 114372850 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
