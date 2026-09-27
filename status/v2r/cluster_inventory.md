# V2R cluster inventory

2026-09-27T09:41:48.257685+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314450694144 available bytes; 82.46% used; 112440736 free inodes.

server1 `/home`: 314450694144 available bytes; 82.46% used; 112440736 free inodes.

server1 `/tmp`: 314450694144 available bytes; 82.46% used; 112440736 free inodes.

server1 `/var/tmp`: 314450694144 available bytes; 82.46% used; 112440736 free inodes.

server1 `/mnt/raid5`: 635438759936 available bytes; 97.09% used; 337424408 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16508510208 available bytes; 99.08% used; 110356916 free inodes.

server2 `/home`: 16508510208 available bytes; 99.08% used; 110356916 free inodes.

server2 `/tmp`: 16508510208 available bytes; 99.08% used; 110356916 free inodes.

server2 `/var/tmp`: 16508510208 available bytes; 99.08% used; 110356916 free inodes.

server2 `/mnt/raid5`: 572760018944 available bytes; 96.04% used; 444741334 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78547763200 available bytes; 95.62% used; 114062910 free inodes.

server3 `/home`: 78547763200 available bytes; 95.62% used; 114062910 free inodes.

server3 `/data`: 1332470681600 available bytes; 81.58% used; 225762165 free inodes.

server3 `/tmp`: 78547763200 available bytes; 95.62% used; 114062910 free inodes.

server3 `/var/tmp`: 78547763200 available bytes; 95.62% used; 114062910 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111050096640 available bytes; 93.80% used; 114372850 free inodes.

server4 `/home`: 111050096640 available bytes; 93.80% used; 114372850 free inodes.

server4 `/data`: 364003057664 available bytes; 94.97% used; 224767146 free inodes.

server4 `/tmp`: 111050096640 available bytes; 93.80% used; 114372850 free inodes.

server4 `/var/tmp`: 111050096640 available bytes; 93.80% used; 114372850 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
