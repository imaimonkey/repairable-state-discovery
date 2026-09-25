# V2R cluster inventory

2026-09-25T16:30:16.573799+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318681370624 available bytes; 82.22% used; 112476333 free inodes.

server1 `/home`: 318681370624 available bytes; 82.22% used; 112476333 free inodes.

server1 `/tmp`: 318681370624 available bytes; 82.22% used; 112476333 free inodes.

server1 `/var/tmp`: 318681370624 available bytes; 82.22% used; 112476333 free inodes.

server1 `/mnt/raid5`: 363913109504 available bytes; 98.33% used; 337544611 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23099318272 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23099318272 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23099318272 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23099318272 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 317805248512 available bytes; 97.80% used; 445070279 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84403544064 available bytes; 95.29% used; 114152669 free inodes.

server3 `/home`: 84403544064 available bytes; 95.29% used; 114152669 free inodes.

server3 `/data`: 133797900288 available bytes; 98.15% used; 225805788 free inodes.

server3 `/tmp`: 84403544064 available bytes; 95.29% used; 114152669 free inodes.

server3 `/var/tmp`: 84403544064 available bytes; 95.29% used; 114152669 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636118528 available bytes; 94.11% used; 114349645 free inodes.

server4 `/home`: 105636118528 available bytes; 94.11% used; 114349645 free inodes.

server4 `/data`: 230032162816 available bytes; 96.82% used; 224934082 free inodes.

server4 `/tmp`: 105636118528 available bytes; 94.11% used; 114349645 free inodes.

server4 `/var/tmp`: 105636118528 available bytes; 94.11% used; 114349645 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
