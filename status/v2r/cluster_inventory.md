# V2R cluster inventory

2026-09-24T08:53:26.565967+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324381528064 available bytes; 81.90% used; 112490229 free inodes.

server1 `/home`: 324381528064 available bytes; 81.90% used; 112490229 free inodes.

server1 `/tmp`: 324381528064 available bytes; 81.90% used; 112490229 free inodes.

server1 `/var/tmp`: 324381528064 available bytes; 81.90% used; 112490229 free inodes.

server1 `/mnt/raid5`: 503997005824 available bytes; 97.69% used; 337717742 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57793458176 available bytes; 96.78% used; 110430936 free inodes.

server2 `/home`: 57793458176 available bytes; 96.78% used; 110430936 free inodes.

server2 `/tmp`: 57793458176 available bytes; 96.78% used; 110430936 free inodes.

server2 `/var/tmp`: 57793458176 available bytes; 96.78% used; 110430936 free inodes.

server2 `/mnt/raid5`: 515689275392 available bytes; 96.44% used; 445179039 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85898125312 available bytes; 95.21% used; 114199581 free inodes.

server3 `/home`: 85898125312 available bytes; 95.21% used; 114199581 free inodes.

server3 `/data`: 167129194496 available bytes; 97.69% used; 225822014 free inodes.

server3 `/tmp`: 85898125312 available bytes; 95.21% used; 114199581 free inodes.

server3 `/var/tmp`: 85898125312 available bytes; 95.21% used; 114199581 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759621120 available bytes; 94.10% used; 114349083 free inodes.

server4 `/home`: 105759621120 available bytes; 94.10% used; 114349083 free inodes.

server4 `/data`: 319737401344 available bytes; 95.58% used; 225273447 free inodes.

server4 `/tmp`: 105759621120 available bytes; 94.10% used; 114349083 free inodes.

server4 `/var/tmp`: 105759621120 available bytes; 94.10% used; 114349083 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
